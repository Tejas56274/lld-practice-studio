# ArchPractice: LLD Practice Platform MVP

> A lightweight practice platform designed to help software engineering learners master Low-Level Design (LLD), submit domain models, and receive instant architectural feedback.

## Demo & Walkthrough
- **Loom Video:** [Watch the 60-second walkthrough link here]

## Tech Stack
- **Backend:** FastAPI, Python, Pydantic
- **Evaluation:** Hybrid engine combining deterministic keyword/class checks with Gemini LLM architectural reasoning
- **Frontend:** Single-page responsive interface styled with Tailwind CSS
- **Testing:** Pytest

## Setup & Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/lld-practice-studio.git
   cd lld-practice-studio
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
   The app will be available at `http://127.0.0.1:8000`.

## API Endpoints
- `GET /api/problems` – Retrieve the list of design problems.
- `POST /api/submit` – Submit a solution for evaluation.
- `GET /api/attempts` – Retrieve the history of all attempts.

## Running Tests
```bash
pytest -q
```