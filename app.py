from typing import Union
from fastapi import FastAPI
from decouple import config

NAME = config('NAME', default="World")

app = FastAPI()

#TODO: Add endpoint as a top-level page.
@app.get("")
def index():
    return {"message": f"Hello {NAME}"}

#TODO: Plus the two parameters and return the result
@app.get("/calculator")
def add(first_number: int, second_number: int):
    return {"first_number": first_number, "second_number": second_number, "result": 0}
