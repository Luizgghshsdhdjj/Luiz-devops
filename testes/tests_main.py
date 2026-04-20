from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_status():
    response = client.get("/status")
    assert response.status_code == 200

def test_teste():
    response = client.get("/teste")
    assert response.status_code == 200
    