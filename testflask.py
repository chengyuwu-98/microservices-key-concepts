import pytest
from flask import Flask
from mainflask import app



@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_main(client):
    rv = client.get("/")
    assert  rv.json== {"message": "Hello"}