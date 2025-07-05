from fastapi import APIRouter, Body
from app.utils import route_ticket

classify_ticket = APIRouter()

@classify_ticket.post("/classify")
def classify(text: str = Body(...)):
    return route_ticket(text)
