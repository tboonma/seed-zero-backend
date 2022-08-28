from models import Item
from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from pydantic import BaseModel
load_dotenv()


NAME = os.getenv('NAME', default="World")

app = FastAPI()

# endpoint as a top-level page.


@app.get("/")
def index():
    return {"message": f"Hello {NAME}"}

# Create a calculator that accept 2 query params and manipulate those 2 values.


@app.get("/calculator/add")
def adder(first_number: int, second_number: int):
    return {"first_number": first_number, "second_number": second_number, "result": first_number+second_number}


@app.get("/calculator/substract")
def subtractor(first_number: int, second_number: int):
    return {"first_number": first_number, "second_number": second_number, "result": first_number-second_number}


@app.get("/calculator/multiply")
def subtractor(first_number: int, second_number: int):
    return {"first_number": first_number, "second_number": second_number, "result": first_number*second_number}


@app.get("/calculator/divide")
def subtractor(first_number: int, second_number: int):
    return {"first_number": first_number, "second_number": second_number, "result": first_number/second_number}


@app.get("/id/{userId}")
def usersInfo(userId: int):
    if userId != 9997:
        raise HTTPException(status_code=404, detail="UserId not found.")

    return {
        "id": userId,
        "name": "Safe",
        "surname": "suk",
    }


class Item(BaseModel):
    name: str
    price: float


@app.post("/item/create/")
def itemCreator(item: Item):
    print(item.name, item.price)
    return item.name, item.price