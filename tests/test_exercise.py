from main import app
from fastapi.testclient import TestClient
from dotenv import load_dotenv
import os
load_dotenv()

client = TestClient(app)


def test_question1():
    response = client.get(os.getenv('ANSWER1', default=""))
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_question2():
    response = client.get("/calculator/add?first_number=1&second_number=2")
    assert response.status_code == 200
    assert response.json() == {"first_number": 1, "second_number": 2, "result": 3}

def test_question3():
    correct_path = list(filter(lambda route: os.getenv('ANSWER3', default="unknown") in route.path, app.routes))
    assert len(correct_path) > 0
