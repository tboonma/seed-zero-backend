from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

import os
load_dotenv()

from models import Item

NAME = os.getenv('NAME', default="World")

app = FastAPI()

# TODO: 1.) Add enudpoint as a top-level page.
@app.get("/")
def index():
    return {"message": f"Hello {NAME}"}

# TODO: 2.) Create a calculator that accept 2 query params and manipulate those 2 values.
@app.get("/calculator/add/")
def adder(first_number: int, second_number: int):
    result = first_number + second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}

@app.get("/calculator/substract")
def subtractor(first_number: int, second_number: int):
    result = first_number - second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


@app.get("/calculator/multiply")
def multiplor(first_number: int, second_number: int):
    result = first_number * second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}

# TODO: (Optional) @app.get("/calculator/divide")
@app.get("/calculator/divide")
def divider(first_number: int, second_number: int):
    result = first_number / second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


# TODO: 3.) Enter a path scheme that accept userId as a path parameter `userId`.
@app.get("/api/v1/users/{userId}")
def usersInfo(userId: int):
    if userId != 9997:
        raise HTTPException(status_code=404, detail="UserId not found.")

    return {
        "id": userId,
        "name": "Safe",
        "surname": "suk",
    }


# TODO: 4.) Make this method to accept `POST` request and request body on path `/item/create/`.
# Example Request Body:
# {
#   "name": "Book",
#   "price": 123,
# }
@app.post("/item/create/")
def itemCreator(item: Item):
    # TODO: Print body's name and price to console.
    return item.name, item.price


