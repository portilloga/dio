from fastapi.testclient import TestClient
from webServer import app

client = TestClient(app)

def test_visa_valid():
    response = client.get("/validateFlag/4111111111111111")
    assert response.status_code == 200
    assert response.json()["isValid"] is True
    assert "Visa" in response.json()["message"]

def test_invalid_number():
    response = client.get("/validateFlag/123")
    assert response.status_code == 200
    assert response.json()["isValid"] is False
    assert "invalid credit card number" in response.json()["message"]

def test_inexistent_flag():
    response = client.get("/validateFlag/1234567890123456")
    assert response.status_code == 200
    assert response.json()["isValid"] is False
    assert "Inexistent credit card flag" in response.json()["message"]

def test_internal_error(monkeypatch):
    def raise_exception(*args, **kwargs):
        raise Exception("Test exception")
    monkeypatch.setattr("CreditCard.CreditCard.validateFlag", raise_exception)
    response = client.get("/validateFlag/4111111111111111")
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal server error"