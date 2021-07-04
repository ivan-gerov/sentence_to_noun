
import pytest

import sys
from app import create_app

@pytest.fixture
def client():
    test_app = create_app()
    with test_app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_parse_sentence_request(client):
    response = client.post("/parse_sentence", data=dict(
        sentence=""
    ))
    assert response.status_code == 200

def test_parse_sentence_request_empty_sentence(client):
    response = client.post("/parse_sentence", data=dict(
        sentence=""
    ))
    assert "Please provide" in str(response.data)

def test_parse_sentence_request_no_alphabetical(client):
    response = client.post("/parse_sentence", data=dict(
        sentence="123123"
    ))
    assert "Please provide" in str(response.data)

def test_parse_sentence_request_successful(client):
    response = client.post("/parse_sentence", data=dict(
        sentence="This is a sentence of tests."
    ))
    assert "Please provide" not in str(response.data)    
    assert "sentence, tests" in str(response.data)    
    