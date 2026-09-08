import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI(title="LLD Practice Platform MVP")

if os.environ.get("GEMINI_API_KEY"):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

PROBLEMS_DB = [
    {
        "id": 1,
        "title": "Design a Parking Lot",
        "description": "Requirements: Support multiple vehicle types (Car, Bike, Truck), multiple levels, different parking spot sizes, automated ticket generation, and a fee calculation strategy."
    },
    {
        "id": 2,
        "title": "Design an Elevator System",
        "description": "Requirements: Multi-car elevator system for a high-rise building, optimal dispatch algorithm, handling internal button presses and external hall requests safely."
    }
]

ATTEMPTS_DB = {}
attempt_counter = 1

class SubmissionRequest(BaseModel):
    problem_id: int
    code: str

class EvaluationResult(BaseModel):
    attempt_id: int
    status: str
    solid_score: int
    design_patterns_detected: List[str]
    feedback_notes: str

def evaluate_code_hybrid(problem_id: int, code: str) -> dict:
    code_lower = code.lower()
    has_class = "class " in code_lower
    
    keyword_matches = 0
    keywords = ["parking", "vehicle", "slot", "ticket", "level"] if problem_id == 1 else ["elevator", "request", "door", "dispatch", "building"]
    for kw in keywords:
        if kw in code_lower:
            keyword_matches += 1

    deterministic_passed = has_class and (keyword_matches >= 2)
    ai_feedback = ""
    solid_score = 3
    patterns_found = []

    try:
        if os.environ.get("GEMINI_API_KEY"):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Review this LLD code for Problem ID {problem_id}:\n{code}\nProvide JSON with 'solid_score' (1-5), 'patterns_found' (list), and 'feedback' (3 concise bullet points)."
            response = model.generate_content(prompt)
            ai_feedback = response.text
        else:
            ai_feedback = "- Good use of separation of concerns.\n- Consider implementing the Strategy Pattern for pricing/dispatch logic.\n- Ensure thread safety for concurrent access."
            solid_score = 4 if deterministic_passed else 2
            patterns_found = ["Strategy Pattern (Suggested)"]
    except Exception as e:
        ai_feedback = f"Fallback triggered: {str(e)}"
        solid_score = 3
        patterns_found = ["Basic Object Structure"]

    return {
        "status": "COMPLETED",
        "solid_score": solid_score,
        "design_patterns_detected": patterns_found,
        "feedback_notes": ai_feedback
    }

@app.get("/api/problems")
def get_problems():
    return PROBLEMS_DB

@app.post("/api/submit", response_model=EvaluationResult)
def submit_solution(submission: SubmissionRequest):
    global attempt_counter
    if not any(p["id"] == submission.problem_id for p in PROBLEMS_DB):
        raise HTTPException(status_code=404, detail="Problem not found")
    
    eval_data = evaluate_code_hybrid(submission.problem_id, submission.code)
    attempt_record = {
        "attempt_id": attempt_counter,
        "problem_id": submission.problem_id,
        "code": submission.code,
        **eval_data
    }
    ATTEMPTS_DB[attempt_counter] = attempt_record
    attempt_counter += 1
    return attempt_record

@app.get("/api/attempts", response_model=List[dict])
def get_all_attempts():
    return list(ATTEMPTS_DB.values())

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>LLD Practice Platform</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-slate-100 font-sans min-h-screen p-6">
        <div class="max-w-6xl mx-auto">
            <header class="mb-8 border-b border-slate-800 pb-4">
                <h1 class="text-2xl font-bold text-emerald-400">ArchPractice: LLD Studio</h1>
                <p class="text-sm text-slate-400">Practice, design, and receive instant architectural feedback.</p>
            </header>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 flex flex-col gap-4">
                    <h2 class="text-lg font-semibold">1. Select Problem & Draft Design</h2>
                    <select id="problemSelect" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-slate-200" onchange="loadProblemDescription()">
                        <option value="1">Design a Parking Lot</option>
                        <option value="2">Design an Elevator System</option>
                    </select>
                    <div id="problemDesc" class="text-xs text-slate-300 bg-slate-900/50 p-3 rounded border border-slate-800"></div>
                    <textarea id="codeEditor" rows="10" class="w-full bg-slate-900 font-mono text-xs border border-slate-700 rounded p-3 text-emerald-300" placeholder="class ParkingLot: ..."></textarea>
                    <button onclick="submitSolution()" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold py-2 px-4 rounded">Submit Design</button>
                </div>
                <div class="flex flex-col gap-6">
                    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 flex-1">
                        <h2 class="text-lg font-semibold mb-4">2. Evaluation & Feedback</h2>
                        <div id="feedbackContainer" class="text-sm text-slate-400 italic">Submit your design to view feedback.</div>
                    </div>
                    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700">
                        <h2 class="text-lg font-semibold mb-2">Attempt History</h2>
                        <div id="historyList" class="text-xs text-slate-400 space-y-2 max-h-40 overflow-y-auto">No prior attempts yet.</div>
                    </div>
                </div>
            </div>
        </div>
        <script>
            async function fetchProblems() {
                const res = await fetch('/api/problems');
                window.problems = await res.json();
                loadProblemDescription();
                loadHistory();
            }
            function loadProblemDescription() {
                const id = document.getElementById('problemSelect').value;
                const prob = window.problems.find(p => p.id == id);
                document.getElementById('problemDesc').innerText = prob.description;
            }
            async function submitSolution() {
                const problem_id = parseInt(document.getElementById('problemSelect').value);
                const code = document.getElementById('codeEditor').value;
                if(!code.trim()) { alert('Enter code first.'); return; }
                document.getElementById('feedbackContainer').innerHTML = '<div class="text-amber-400 animate-pulse">Evaluating architecture...</div>';
                const res = await fetch('/api/submit', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ problem_id, code })
                });
                const data = await res.json();
                document.getElementById('feedbackContainer').innerHTML = `
                    <div class="space-y-3">
                        <div class="flex justify-between items-center bg-slate-900 p-2 rounded border border-slate-700">
                            <span>SOLID Score:</span><span class="text-emerald-400 font-bold">${data.solid_score} / 5</span>
                        </div>
                        <div class="bg-slate-900 p-2 rounded border border-slate-700">
                            <span class="block mb-1 font-semibold">Detected Patterns:</span>
                            <span class="text-xs text-cyan-300">${data.design_patterns_detected.join(', ')}</span>
                        </div>
                        <div class="bg-slate-900 p-3 rounded border border-slate-700">
                            <span class="block mb-1 font-semibold">Feedback:</span>
                            <pre class="text-xs text-slate-300 whitespace-pre-wrap font-sans">${data.feedback_notes}</pre>
                        </div>
                    </div>`;
                loadHistory();
            }
            async function loadHistory() {
                const res = await fetch('/api/attempts');
                const attempts = await res.json();
                if(attempts.length === 0) return;
                let html = '';
                attempts.reverse().forEach(att => {
                    html += `<div class="bg-slate-900 p-2 rounded border border-slate-700 flex justify-between"><span>Attempt #${att.attempt_id}</span><span class="text-emerald-400 font-bold">Score: ${att.solid_score}/5</span></div>`;
                });
                document.getElementById('historyList').innerHTML = html;
            }
            fetchProblems();
        </script>
    </body>
    </html>
    """