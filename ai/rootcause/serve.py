from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title='resilo-rootcause')
model_data = joblib.load('models/root_cause.joblib')
label_map = {0:'OOM',1:'CONFIG',2:'DEPENDENCY',3:'CODE_BUG'}

class Req(BaseModel):
    mem_pct: float = 0.0
    cpu_pct: float = 0.0
    error_rate: float = 0.0
    recent_config_change: int = 0

@app.get('/healthz')
def health():
    return {'status':'ok'}

@app.post('/root_cause')
def root_cause(req: Req):
    features = [req.mem_pct, req.cpu_pct, req.error_rate, req.recent_config_change]
    model = model_data['model']
    pred = int(model.predict([features])[0])
    probs = model.predict_proba([features])[0].tolist()
    rec = [{'type':'scale','replicas':3}] if pred==0 else [{'type':'rollback'}]
    return {'cause': label_map[pred], 'probs': probs, 'features': features, 'recommended_actions': rec}
