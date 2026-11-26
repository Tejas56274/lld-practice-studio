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
3. **Configure the Gemini API key (optional)**
   ```bash
   export GEMINI_API_KEY=your_gemini_api_key   # On Windows use `set GEMINI_API_KEY=your_gemini_api_key`
   ```
4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```
   The UI will be available at `http://127.0.0.1:8000/`.

## Running Tests
```bash
pytest -q
```