import pytest
from flask import Flask

app = Flask(__name__)



@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_main(client):
    rv = client.get("/")
    assert {"message": "Hello"} == rv.data