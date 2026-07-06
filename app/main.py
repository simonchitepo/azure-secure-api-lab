from enum import Enum
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


class Exposure(str, Enum):
    public = "public"
    internal = "internal"
    private = "private"


class DataClassification(str, Enum):
    public = "public"
    internal = "internal"
    confidential = "confidential"


class RiskRequest(BaseModel):
    asset_name: str = Field(..., min_length=2, max_length=80)
    exposure: Exposure
    data_classification: DataClassification
    authentication_required: bool = True
    internet_accessible: bool = False


app = FastAPI(
    title="Azure Secure API Lab",
    description="Cloud Security / DevSecOps portfolio API.",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "project": "Azure Secure API Lab",
        "purpose": "Cloud Security / DevSecOps portfolio project",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": ENVIRONMENT,
        "version": APP_VERSION,
    }


@app.get("/security-status")
def security_status():
    return {
        "hardcoded_secrets": "not used",
        "configuration": "environment variables",
        "planned_controls": [
            "Azure Key Vault",
            "Managed Identity",
            "Application Insights",
            "Log Analytics",
            "Terraform",
            "GitHub Actions security checks",
        ],
    }


@app.post("/risk-check")
def risk_check(request: RiskRequest):
    score = 0

    if request.exposure == Exposure.public:
        score += 3
    elif request.exposure == Exposure.internal:
        score += 2
    else:
        score += 1

    if request.data_classification == DataClassification.confidential:
        score += 3
    elif request.data_classification == DataClassification.internal:
        score += 2
    else:
        score += 1

    if request.internet_accessible:
        score += 2

    if not request.authentication_required:
        score += 2

    if score >= 8:
        risk = "high"
    elif score >= 5:
        risk = "medium"
    else:
        risk = "low"

    return {
        "asset_name": request.asset_name,
        "risk_score": score,
        "risk_level": risk,
        "recommendations": [
            "Use least privilege IAM",
            "Avoid public exposure unless required",
            "Store secrets outside source code",
            "Enable logging and monitoring",
            "Document threat model and residual risks",
        ],
    }
