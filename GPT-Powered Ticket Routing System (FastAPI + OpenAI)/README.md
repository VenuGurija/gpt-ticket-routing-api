# GPT-Powered Ticket Routing API

A lightweight FastAPI service that routes support tickets using OpenAI GPT-4 prompts. Designed as a fallback for manual triage, with classification logic, minimal infra, and JWT-based protection (optional).

## 🔧 Tech Stack
- FastAPI
- OpenAI API (GPT-4)
- Python 3.10
- Docker (optional)

## 🚀 How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
