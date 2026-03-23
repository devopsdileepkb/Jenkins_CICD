# Jenkins_CICD

# Jenkins_CICD – Secure Notes App

## Overview
A Python Flask app with login/signup and notes functionality, deployed via:
- Jenkins (CI/CD pipeline)
- Docker (containerization)
- Terraform (AWS EKS infrastructure)
- Kubernetes (orchestration with HA)

## Folder Structure
- `src/` → Application code
- `docker/` → Dockerfile
- `jenkins/` → Jenkinsfile
- `iac/` → Terraform IaC
- `k8s/` → Kubernetes manifests
- `docs/` → Documentation

## Deployment Flow
1. Code pushed to GitHub.
2. Jenkins pipeline builds Docker image, runs tests, pushes to registry.
3. Terraform provisions EKS cluster.
4. Kubernetes manifests applied to EKS → HA deployment.

## How to Run Locally
```bash
cd src
pip install -r requirements.txt
python app.py