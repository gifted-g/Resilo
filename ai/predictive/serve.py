from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np

app = FastAPI(title='resilo-predictor')
model_data = joblib.load('models/predict_failure.joblib')

class PredictReq(BaseModel):
    test_fail_rate: float = 0.0
    cpu_slope: float = 0.0
    files_changed: float = 0.0
    deploy_frequency: float = 0.0

@app.get('/healthz')
def health():
    return {'status':'ok'}

@app.post('/predict')
def predict(req: PredictReq):
    features = [req.test_fail_rate, req.cpu_slope, req.files_changed, req.deploy_frequency]
    model = model_data['model']
    prob = float(model.predict_proba([features])[0,1])
    action = 'hold_deploy' if prob > 0.6 else 'proceed'
    return {'risk': prob, 'action': action, 'explanation': {'features': features}}
