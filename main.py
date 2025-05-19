from fastapi import FastAPI
from pydantic import BaseModel
from utils import analyze_message  # <-- this is new

app = FastAPI()

class Ticket(BaseModel):
    message: str

@app.post("/analyze")
def analyze(ticket: Ticket):
    return analyze_message(ticket.message)
