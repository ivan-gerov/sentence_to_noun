import pytest

import sys
from app import create_app


@pytest.fixture
def client():
    test_app = create_app()
    with test_app.test_client() as client:
        yield client


def test_home_page(client):
    """Test home page route"""
    response = client.get("/")
    assert response.status_code == 200


def test_parse_sentence_request(client):
    """Tests parse_sentence request route is working."""
    response = client.post("/parse_sentence", data=dict(sentence=""))
    assert response.status_code == 200


def test_parse_sentence_request_empty_sentence(client):
    """
    Tests that an empty sentence returns a
    "Please provide a valid sentence" message to the client.
    """
    response = client.post("/parse_sentence", data=dict(sentence=""))
    assert "Please provide" in str(response.data)


def test_parse_sentence_request_no_alphabetical(client):
    """
    Tests that a sentence that doesn't contain alphabetical
    characters will return a "Please provide valid sentence"
    message to the client.
    """
    response = client.post("/parse_sentence", data=dict(sentence="123123"))
    assert "Please provide" in str(response.data)


def test_parse_sentence_request_successful(client):
    """
    Tests that a valid sentence will return the extracted
    nouns to the client.
    """
    response = client.post(
        "/parse_sentence", data=dict(sentence="This is a sentence of tests.")
    )
    assert "Please provide" not in str(response.data)
    assert "sentence, tests" in str(response.data)
