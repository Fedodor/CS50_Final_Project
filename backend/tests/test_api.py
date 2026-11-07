import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_cryptocurrencies():
    response = client.get("/cryptocurrencies")
    assert response.status_code == 200
    # This will fail without a valid API key, but we're testing the endpoint structure