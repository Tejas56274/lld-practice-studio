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
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. **(Optional) Configure Gemini API key**
   If you have a Gemini API key, export it so the hybrid evaluator can use the LLM:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
   The application will fall back to a deterministic evaluation when the key is not set.
4. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000` and the UI at the root path (`/`).
5. **Run the test suite**
   ```bash
   pytest -q
   ```

## API Endpoints
- `GET /api/problems` – Retrieve the list of design problems.
- `POST /api/submit` – Submit a solution for evaluation (expects JSON with `problem_id` and `code`).
- `GET /api/attempts` – List all submission attempts made during the session.

## License
MIT License