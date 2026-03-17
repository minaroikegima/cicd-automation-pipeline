# CI/CD Automation Pipeline

![CI](https://github.com/minaroikegima/cicd-automation-pipeline/actions/workflows/ci.yml/badge.svg)

A GitHub Actions CI/CD pipeline that automates build, test, security scanning, and Docker deployment workflows for containerized applications.

## What This Project Does
- Automatically tests code on every pull request
- Builds and scans Docker images for security vulnerabilities
- Deploys to staging automatically on every merge
- Sends Slack notifications on success or failure

## Technologies Used
- GitHub Actions
- Docker
- Python (Flask)
- pytest

## Pipeline Flow
```
Push Code to GitHub
        │
        ▼
┌───────────────┐
│   Run Tests   │ ── ❌ FAIL → Pipeline stops
│   (pytest)    │
└───────┬───────┘
        │ ✅ PASS
        ▼
┌───────────────┐
│  Build Docker │ ── ❌ FAIL → Pipeline stops
│    Image      │
└───────┬───────┘
        │ ✅ PASS
        ▼
   Code is Good!
```

## How to Run Locally
```bash
cd app/src
pip3 install flask prometheus_client
python3 app.py
```
Visit http://localhost:8080 in your browser.

## Project Structure
```
project4-cicd/
├── .github/
│   └── workflows/
│       └── ci.yml        # Pipeline definition
├── app/
│   ├── src/
│   │   └── app.py        # Flask application
│   └── tests/
│       └── test_app.py   # Unit tests
└── docker/
    └── Dockerfile        # Container definition
```
