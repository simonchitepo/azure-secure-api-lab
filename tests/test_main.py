from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_security_status_endpoint():
    response = client.get("/security-status")
    assert response.status_code == 200
    data = response.json()
    assert data["hardcoded_secrets"] == "not used"


def test_risk_check_high_risk():
    payload = {
        "asset_name": "public-customer-api",
        "exposure": "public",
        "data_classification": "confidential",
        "authentication_required": False,
        "internet_accessible": True
    }

    response = client.post("/risk-check", json=payload)
    assert response.status_code == 200
    assert response.json()["risk_level"] == "high"
