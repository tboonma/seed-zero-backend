from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name: str
    price: float
    
class Message(BaseModel):
    detail: str

class CalculatorResponse(BaseModel):
    first_number: int
    second_number: int
    result: float
    
class UserInfo(BaseModel):
    id: int
    name: str
    surname: str