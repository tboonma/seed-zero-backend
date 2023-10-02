from http.client import HTTPException
from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

from models import Item, Message, CalculatorResponse, UserInfo

NAME = os.getenv("NAME", default="World")

app = FastAPI()

@app.get("/")
def index():
    return {"message": f"Hello {NAME}"}


@app.get("/calculator/add")
def adder(first_number: int, second_number: int) -> CalculatorResponse:
    # TODO: Start here
    return {
        "first_number": first_number,
        "second_number": second_number,
        "result": first_number + second_number,
    }


@app.get("/calculator/substract")
def subtractor(first_number: int, second_number: int) -> CalculatorResponse:
    # TODO: Start here
    return {
        "first_number": first_number,
        "second_number": second_number,
        "result": first_number - second_number,
    }


@app.get("/calculator/multiply")
def multiplier(first_number: int, second_number: int) -> CalculatorResponse:
    return {
        "first_number": first_number,
        "second_number": second_number,
        "result": first_number * second_number,
    }


@app.get("/calculator/divide", responses={status.HTTP_400_BAD_REQUEST: {"model": Message}})
def diviver(
    first_number: int,
    second_number: int,
) -> CalculatorResponse:
    if second_number != 0:
        return {
            "first_number": first_number,
            "second_number": second_number,
            "result": first_number / second_number,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Can't divide by zero"
        )


@app.get("/userId", responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
def usersInfo(userId: int) -> UserInfo:
    if userId != 9997:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserId not found.")

    return {
        "id": userId,
        "name": "Safe",
        "surname": "suk",
    }


@app.post("/item/create", status_code=status.HTTP_204_NO_CONTENT)
def itemCreator(item: Item):
    print(f"name is {item.name} , price is {item.price}")
