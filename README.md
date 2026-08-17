# Azure Secure API Lab

## 1. Problem Statement

Many beginner cloud projects only prove that an application can run. They do not prove that the application is secure, monitored, documented, or deployed with proper cloud security controls.

This project demonstrates how to build and deploy a small API using a cloud security and DevSecOps mindset.

The goal is to show practical understanding of:

- Secure Azure deployment
- IAM and least privilege
- Secrets management
- HTTPS/TLS
- Logging and monitoring
- Threat modeling
- Security controls documentation
- GitHub Actions CI
- Future Terraform infrastructure

This project is intentionally small so the main focus stays on security, cloud architecture, documentation, and evidence.

---

## 2. What I Built

I built a small FastAPI application that exposes security-focused endpoints.

The API includes:

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Project overview |
| `/health` | GET | Health check endpoint |
| `/security-status` | GET | Shows current and planned security controls |
| `/risk-check` | POST | Accepts asset details and returns a simple risk score |

The API is used as a practical cloud security lab. The application logic is simple, but the surrounding engineering work is the important part: deployment, IAM, documentation, monitoring, secrets handling, and threat modeling.

---

## 3. Project Goal

The goal of this repository is to prove that I can deploy a production-style cloud application securely, not just write code.

This project is part of my Cloud Security / DevSecOps portfolio and is designed to show evidence for junior roles such as:

- Junior Cloud Security Analyst
- Junior DevSecOps Engineer
- Cloud Support Security
- Junior Platform Engineer
- IAM / Vulnerability Analyst

---

## 4. Architecture Summary

Users access the API over HTTPS. The API runs on Azure App Service. Application configuration is handled through environment variables at first, then moved toward Azure Key Vault using Managed Identity.

Application telemetry and logs will be sent to Azure Application Insights and Log Analytics. GitHub Actions will run tests automatically, and Terraform will later be used to define the Azure infrastructure.

High-level architecture:

```text
User
  |
  | HTTPS
  v
Azure App Service
  |
  | Runs FastAPI application
  v
FastAPI API
  |
  | Future secure secret access
  v
Azure Managed Identity ---> Azure Key Vault

Azure App Service ---> Application Insights ---> Log Analytics

GitHub Repository ---> GitHub Actions ---> Tests / Future Deployment
```

---

## 5. Technologies Used

| Area | Technology |
|---|---|
| Cloud Provider | Microsoft Azure |
| Hosting | Azure App Service |
| Backend Framework | FastAPI |
| Language | Python |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Secrets Management | Azure Key Vault |
| Identity | Azure Managed Identity |
| Monitoring | Azure Application Insights |
| Logs | Azure Log Analytics |
| Infrastructure as Code | Terraform |
| Documentation | Markdown |
| Diagrams | Mermaid |

---

## 6. Security Controls

| Control | Why It Matters | Status |
|---|---|---|
| No hardcoded secrets | Prevents passwords, API keys, tokens, and cloud credentials from being exposed in GitHub | In progress |
| Least privilege IAM | Reduces damage if one identity, service, or account is compromised | Planned |
| HTTPS/TLS | Protects API traffic between the user and the cloud app | Planned |
| Logging | Helps detect errors, attacks, suspicious requests, and failed access attempts | Planned |
| Threat model | Identifies possible attack paths and documents mitigations | In progress |
| Environment variables | Keeps configuration separate from application code | In progress |
| Azure Key Vault | Stores sensitive secrets outside source code | Planned |
| Managed Identity | Allows the app to access Azure resources without storing credentials in code | Planned |
| GitHub Actions CI | Automatically tests the project before changes are accepted | In progress |
| Terraform | Makes cloud infrastructure reproducible and easier to review | Planned |

---

## 7. Repository Structure

```text
azure-secure-api-lab/
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── THREAT_MODEL.md
│   ├── SECURITY_CONTROLS.md
│   ├── logs-and-alerts.md
│   └── cost-control.md
├── diagrams/
│   └── architecture.mmd
├── screenshots/
├── terraform/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml
├── README.md
├── SECURITY.md
├── requirements.txt
├── requirements-dev.txt
├── .env.example
└── .gitignore
```

---

## 8. Local Setup

### 8.1 Clone the Repository

```bash
git clone https://github.com/simonchitepo/azure-secure-api-lab.git
cd azure-secure-api-lab
```

### 8.2 Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

For Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 8.3 Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 8.4 Run the API Locally

```bash
uvicorn app.main:app --reload
```

The API should now run at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 9. Run Tests

Run:

```bash
pytest
```

Expected result:

```text
All tests should pass.
```

The tests check:

- The health endpoint works
- The security status endpoint works
- The risk-check endpoint returns the expected risk level

---

## 10. API Usage

### 10.1 Health Check

Request:

```bash
curl http://127.0.0.1:8000/health
```

Example response:

```json
{
  "status": "ok",
  "environment": "local",
  "version": "0.1.0"
}
```

---

### 10.2 Security Status

Request:

```bash
curl http://127.0.0.1:8000/security-status
```

Example response:

```json
{
  "hardcoded_secrets": "not used",
  "configuration": "environment variables",
  "planned_controls": [
    "Azure Key Vault",
    "Managed Identity",
    "Application Insights",
    "Log Analytics",
    "Terraform",
    "GitHub Actions security checks"
  ]
}
```

---

### 10.3 Risk Check

Request body:

```json
{
  "asset_name": "public-customer-api",
  "exposure": "public",
  "data_classification": "confidential",
  "authentication_required": false,
  "internet_accessible": true
}
```

Example response:

```json
{
  "asset_name": "public-customer-api",
  "risk_score": 10,
  "risk_level": "high",
  "recommendations": [
    "Use least privilege IAM",
    "Avoid public exposure unless required",
    "Store secrets outside source code",
    "Enable logging and monitoring",
    "Document threat model and residual risks"
  ]
}
```

---

## 11. Environment Variables

The project uses environment variables for configuration.

Example `.env.example`:

```text
ENVIRONMENT=local
APP_VERSION=0.1.0
```

Important rule:

```text
.env must never be committed to GitHub.
```

The `.gitignore` file should include:

```text
.env
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

---

## 12. Secrets Management Approach

Current version:

- No real secrets are required.
- `.env` is ignored by Git.
- `.env.example` documents safe placeholder values.
- No passwords, API keys, or Azure credentials should be committed.

Planned Azure version:

- Use Azure Key Vault for secrets.
- Use Azure Managed Identity so the App Service can access Key Vault without storing credentials in code.
- Use least privilege permissions so the app can only read the secrets it needs.

---

## 13. IAM and Least Privilege Plan

The IAM goal is to avoid giving broad permissions to services or users.

Planned access model:

| Identity | Permission | Reason |
|---|---|---|
| Azure App Service Managed Identity | Read selected Key Vault secrets | Allows the app to retrieve secrets securely |
| GitHub Actions deployment identity | Limited deployment permission | Allows CI/CD deployment without excessive access |
| Developer account | Temporary admin/contributor access during lab setup | Used only during learning and setup |

Future improvement:

- Replace broad access with more specific role assignments.
- Document screenshots of IAM role assignments.
- Add least privilege explanation in `docs/SECURITY_CONTROLS.md`.

---

## 14. HTTPS/TLS Plan

The deployed API should be accessed through HTTPS.

Planned evidence:

- Screenshot of the deployed API using `https://`
- Screenshot of browser lock icon
- Documentation explaining that API traffic should not be sent over plain HTTP

Future improvement:

- Add custom domain
- Add managed certificate
- Document TLS configuration

---

## 15. Logging and Monitoring Plan

Logging is required so security events and operational issues can be investigated.

Planned logging evidence:

- Azure Application Insights enabled
- Log Analytics workspace connected
- Screenshot of requests to `/health`
- Screenshot of requests to `/risk-check`
- Screenshot of errors or test traffic

Planned log documentation:

```text
docs/logs-and-alerts.md
```

This file will explain:

- What logs are collected
- Where logs are stored
- What security questions the logs can answer
- What alerts should be created later

---

## 16. Threat Model

The project includes a threat model file:

```text
docs/THREAT_MODEL.md
```

The threat model covers:

- Assets
- Actors
- Entry points
- Attack paths
- Mitigations
- Residual risks

Example threats:

| Threat | Example Attack Path | Mitigation |
|---|---|---|
| Hardcoded secret exposure | Secret committed to GitHub | Use `.env`, `.gitignore`, and Azure Key Vault |
| Public endpoint abuse | Attacker sends repeated requests | Add logging, rate limiting, and alerts |
| Excessive IAM permissions | App identity has too much access | Use least privilege IAM |
| Missing logs | Attack happens with no investigation trail | Enable Application Insights and Log Analytics |
| Sensitive data in logs | App logs secrets or private data | Avoid logging secrets and review log fields |

---

## 17. Cloud Deployment Plan

Target Azure services:

| Azure Service | Purpose |
|---|---|
| Azure Resource Group | Groups all project resources |
| Azure App Service Plan | Hosting plan for the web app |
| Azure App Service | Hosts the FastAPI API |
| Azure Key Vault | Stores secrets |
| Managed Identity | Allows secure access to Key Vault |
| Application Insights | Monitors application behavior |
| Log Analytics | Stores and queries logs |

Deployment steps will be documented after the first Azure deployment.

---

## 18. GitHub Actions CI

The repository includes a GitHub Actions workflow:

```text
.github/workflows/ci.yml
```

The CI workflow will:

- Checkout the repository
- Set up Python
- Install dependencies
- Run tests with `pytest`

Current CI status:

```text
In progress
```

Planned future CI improvements:

- Add linting
- Add secret scanning
- Add dependency scanning
- Add Docker image scanning
- Add deployment workflow
- Add branch protection notes

---

## 19. Evidence To Add

This repository should contain evidence that proves the project works.

Planned evidence:

| Evidence | File or Folder |
|---|---|
| Architecture diagram | `diagrams/architecture.mmd` |
| Architecture screenshot | `screenshots/architecture-preview.png` |
| Local API docs screenshot | `screenshots/local-api-docs.png` |
| Azure App Service screenshot | `screenshots/azure-app-service.png` |
| HTTPS screenshot | `screenshots/https-working.png` |
| Application logs screenshot | `screenshots/application-insights-logs.png` |
| GitHub Actions screenshot | `screenshots/github-actions-ci.png` |
| Threat model | `docs/THREAT_MODEL.md` |
| Security controls | `docs/SECURITY_CONTROLS.md` |
| Cost notes | `docs/cost-control.md` |

---

## 20. Screenshots

Screenshots will be added as the project progresses.

Required screenshots:

- Local API running
- FastAPI `/docs` page
- Test results
- GitHub Actions passing
- Azure App Service overview
- HTTPS working
- Application Insights logs
- Architecture diagram

---

## 21. Cost Control Notes

Cloud resources can cost money, so cost control is part of the project.

Cost control rules:

- Use a small Azure App Service SKU where possible.
- Delete unused resources.
- Keep all resources inside one Resource Group.
- Use clear resource names.
- Document what each resource is used for.
- Destroy test resources when not needed.
- Add Terraform destroy instructions later.

The cost control document will be stored here:

```text
docs/cost-control.md
```

---

## 22. Current Status

| Area | Status |
|---|---|
| Local FastAPI app | Done |
| Unit tests | Done |
| README documentation | In progress |
| Security controls table | Done |
| Architecture outline | In progress |
| Threat model | In progress |
| Azure deployment | Planned |
| HTTPS evidence | Planned |
| Logging evidence | Planned |
| Terraform | Planned |
| GitHub Actions | In progress |

---

## 23. Lessons Learned

Current lessons:

- A cloud security project does not need to be complex to be useful.
- The value comes from showing secure design, documentation, controls, and evidence.
- A small API can be used to demonstrate IAM, secrets management, logging, monitoring, and deployment practices.
- A strong README helps recruiters understand the project quickly.

More lessons will be added as the project develops.

---

## 24. Limitations

This is a portfolio lab, not a full production system.

Current limitations:

- No authentication yet
- No database yet
- No rate limiting yet
- No Web Application Firewall yet
- No Terraform deployment yet
- No Azure Key Vault integration yet
- No production monitoring alerts yet

These limitations are documented intentionally to show security awareness and realistic project scope.

---

## 25. Next Improvements

Planned next steps:

1. Deploy the API to Azure App Service.
2. Confirm HTTPS access.
3. Enable Azure Application Insights.
4. Add screenshots to the `screenshots/` folder.
5. Write `docs/SECURITY_CONTROLS.md`.
6. Improve `docs/THREAT_MODEL.md`.
7. Add Terraform files.
8. Add GitHub Actions security checks.
9. Add Azure Key Vault.
10. Add Managed Identity.
11. Document least privilege IAM.
12. Add final project summary for recruiters.

---

## 26. Interview Explanation

A short explanation of this project:

> I built a small FastAPI security API and used it as a cloud security deployment lab on Azure. The purpose was not just to deploy an app, but to document and apply security controls such as no hardcoded secrets, least privilege IAM, HTTPS, logging, threat modeling, and future Key Vault integration. I also added tests, GitHub Actions, architecture documentation, and planned Terraform infrastructure so the project shows practical Cloud Security and DevSecOps skills.

---

## 27. Final Portfolio Outcome

When finished, this project should prove:

- I can build and deploy a small API.
- I understand basic cloud security controls.
- I can document architecture clearly.
- I can write a basic threat model.
- I can think about IAM and least privilege.
- I can avoid hardcoded secrets.
- I can collect evidence through screenshots and logs.
- I can use GitHub professionally for security-focused projects.

---

## 28. Author

Simon Chitepo

Computer Science student focused on Cloud Security, DevSecOps, IAM, Azure, secure deployment, and security operations.
## Security Controls

| Control ID | Category | Description | Implementation | Status |
|---|---|---|---|---|
| SC-01 | Identity & Access Management | Least-privilege access to Azure resources | Azure IAM roles scoped per service, no broad Owner/Contributor grants | Implemented |
| SC-02 | Secrets Management | No secrets in code or config | Azure Key Vault for API keys/connection strings | Implemented |
| SC-03 | Transport Security | Encrypt data in transit | HTTPS enforced on App Service | Implemented |
| SC-04 | Logging & Monitoring | Detect and investigate incidents | Azure Monitor / App Service diagnostic logging enabled | Implemented |
| SC-05 | Infrastructure as Code | Reproducible, auditable environment | Terraform manages all cloud resources | Implemented |
| SC-06 | CI/CD Security | Prevent insecure deploys | GitHub Actions pipeline with secret scanning / dependency checks | In progress |
| SC-07 | Threat Modeling | Document known attack surface | Threat model doc included in repo | Planned |
