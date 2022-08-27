from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from decouple import config

from models import Item

NAME = config('NAME', default="World")

app = FastAPI()

# TODO: 1.) Add endpoint as a top-level page.
@app.get("/")
def index():
    return {"message": f"Hello {NAME}"}

# TODO: 2.) Create a calculator that accept 2 query params and manipulate those 2 values.
@app.get("/calculator/add")
def adder(first_number: int, second_number: int):
    # TODO: Start here
    return {"first_number": first_number, "second_number": second_number, "result": 0}

@app.get("/calculator/substract")
def subtractor(first_number: int, second_number: int):
    # TODO: Start here
    return {"first_number": first_number, "second_number": second_number, "result": 0}

# TODO: (Optional) @app.get("/calculator/multiply")

# TODO: (Optional) @app.get("/calculator/divide")



# TODO: 3.) Enter a path scheme that accept userId as a path parameter `userId`.
@app.get("")
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
# @app.????(???)
def itemCreator(item: Item):
    # TODO: Print body's name and price to console.
    return item.name, item.price


