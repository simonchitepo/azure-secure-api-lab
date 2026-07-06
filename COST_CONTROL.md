# Deployment Notes

## Prerequisites

- Azure CLI installed.
- Terraform installed.
- Docker installed.
- Azure subscription with permission to create resource groups, role assignments, Container Apps, ACR, Key Vault, and Log Analytics.

## 1. Login

```bash
az login
az account show
```

## 2. Deploy base cloud resources

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

The first apply may deploy the Microsoft sample image. This lets you prove the Azure resources work before pushing your own image.

## 3. Build and push your API image

From the project root:

```bash
ACR_NAME="<acrNameFromAzure>"
az acr login --name "$ACR_NAME"
az acr build --registry "$ACR_NAME" --image secure-azure-api-lab:v1 .
```

Get the login server:

```bash
az acr show --name "$ACR_NAME" --query loginServer -o tsv
```

## 4. Re-apply Terraform with your image

```bash
terraform apply -var="container_image=<loginServer>/secure-azure-api-lab:v1"
```

## 5. Test deployed API

```bash
curl https://<container-app-fqdn>/health
curl https://<container-app-fqdn>/api/security-status
```

## 6. Evidence to capture

Save screenshots in `screenshots/`:

- Azure resource group.
- Container App overview.
- App HTTPS URL returning `/health`.
- Log Analytics query output.
- GitHub Actions run passing.
- Trivy/Gitleaks scan output.

## 7. Clean up to control costs

```bash
terraform destroy
```
