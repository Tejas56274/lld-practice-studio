# ArchPractice: LLD Practice Platform MVP

> A lightweight practice platform designed to help software engineering learners master Low-Level Design (LLD), submit domain models, and receive instant architectural feedback.

## Demo & Walkthrough
- **Loom Video:** [Watch the 60‑second walkthrough link here]

## Tech Stack
- **Backend:** FastAPI, Python, Pydantic
- **Evaluation:** Hybrid engine combining deterministic keyword/class checks with Gemini LLM architectural reasoning
- **Frontend:** Single‑page responsive interface styled with Tailwind CSS
- **Testing:** Pytest

## Setup & Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/lld-practice-studio.git
   cd lld-practice-studio
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the Gemini API key** (if you want AI‑enhanced feedback)
   ```bash
   export GEMINI_API_KEY=your_gemini_api_key   # On Windows: set GEMINI_API_KEY=your_gemini_api_key
   ```
5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

6. **Open the UI**
   Navigate to `http://127.0.0.1:8000` in your browser. The UI loads the problem list, lets you write a class design, submit it, and view feedback.

## Running Tests
```bash
pytest -q
```
All tests should pass, confirming the basic API functionality.

## Project Structure
- `main.py` – FastAPI application with endpoints for problems, submissions, and attempts.
- `README.md` – This documentation.
- `test_app.py` – Pytest suite covering the core API routes.
- `AI_USAGE.md` & `RESEARCH.md` – Design rationale and AI integration notes.

---
*Feel free to open issues or submit pull requests for enhancements!*