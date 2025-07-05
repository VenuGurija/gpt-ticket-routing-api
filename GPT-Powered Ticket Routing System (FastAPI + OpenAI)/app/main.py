
### 📄 `app/main.py`

from fastapi import FastAPI
from app.router import classify_ticket

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Service up"}

app.include_router(classify_ticket)
