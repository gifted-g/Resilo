# INSTALL.md - Resilo (Local Development)

## Prerequisites
- Git
- Docker & Docker Compose
- Node.js 18+ and npm
- Go 1.21+
- Python 3.10+ and pip

## Clone
```bash
git clone <repo-url>
cd resilo_full
```

## AI services (Python)
Create venv and install deps:
```bash
cd ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Train models (example):
```bash
cd ai/predictive
python train.py
```

Serve a model locally:
```bash
# from ai/predictive
uvicorn serve:app --port 8080 --host 0.0.0.0
```

## Backend (Go)
From repo root:
```bash
cd backend/control-plane
go mod tidy
go run main.go
# server listens on :8080
```

## Frontend (Next.js + Tailwind)
```bash
cd frontend
npm install
npm run dev
# open http://localhost:3000
```

## Bring up everything with Docker Compose (optional)
From repo root:
```bash
docker compose -f infra/docker-compose.yml up --build
```
This will build and run AI services and the Go control-plane for local dev.

