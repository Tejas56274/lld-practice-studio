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
   pip install fastapi uvicorn pydantic google-generativeai
   ```
4. **Configure the Gemini API key** (if you want AI‑enhanced feedback)
   ```bash
   export GEMINI_API_KEY=your_gemini_api_key   # Linux/macOS
   set GEMINI_API_KEY=your_gemini_api_key      # Windows CMD
   ```
5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```
   The UI will be available at `http://127.0.0.1:8000/`.

## Running Tests
```bash
pytest -q
```

## Project Structure
- `main.py` – FastAPI application with problem catalog, submission endpoint, and simple HTML UI.
- `test_app.py` – Basic integration tests using FastAPI's TestClient.
- `README.md` – This documentation.
- `AI_USAGE.md` & `RESEARCH.md` – Design rationale and AI‑assisted decisions.

## License
MIT License (c) 2024 ArchPractice.
