from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np

app = FastAPI(title='resilo-testprio')
models = joblib.load('models/test_prio_models.joblib')

class Req(BaseModel):
    changed_files_vector: list

@app.get('/healthz')
def health():
    return {'status':'ok'}

@app.post('/prioritize')
def prioritize(req: Req):
    vec = np.array(req.changed_files_vector).reshape(1,-1)
    scores = {}
    for k,clf in models.items():
        prob = float(clf.predict_proba(vec)[0,1])
        scores[k] = prob
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    return {'ranked': ranked}
