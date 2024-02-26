# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
# from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, errors
from app.conversation import conversation

class Input(BaseModel):
    # human_input: str
    age: str
    goal: str
    level: str
    days: str
    weeks:str
    time: str
    style: str
    gym: str
    health: str
    current_week:str

class Output(BaseModel):
    output: str

app=FastAPI()

@app.post("/conversation")
async def input(input: Input):
    output = Output(output=conversation(input.age, input.goal, input.level, input.days, input.weeks, input.time, input.style, input.gym, input.health,input.current_week))
    return output

origins = [
    "<http://localhost>",
    "<http://localhost:5173>",
        "...Your Domains..."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

