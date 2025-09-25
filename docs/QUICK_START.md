# Quick Start (Local)

1. Setup Python venv and install:
   ```bash
   cd ai
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Train models:
   ```bash
   ./train_all.sh
   ```
3. Run AI services (in separate terminals):
   ```bash
   cd ai/predictive; uvicorn serve:app --port 8080 --host 0.0.0.0
   cd ai/rootcause; uvicorn serve:app --port 8081 --host 0.0.0.0
   cd ai/testprio; uvicorn serve:app --port 8082 --host 0.0.0.0
   cd ai/assistant; uvicorn serve:app --port 8083 --host 0.0.0.0
   ```
4. Run backend:
   ```bash
   cd backend/control-plane; go run main.go
   ```
5. Run frontend:
   ```bash
   cd frontend; npm install; npm run dev
   ```
Open http://localhost:3000/deployments and use the assistant.
