from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='resilo-ai-assistant')

DOCS = [
    {'id':'log1','text':'[ERROR] OOMKilled container resilo-api at 2025-09-01 10:00 UTC'},
    {'id':'log2','text':'[WARN] Config map updated for resilo-api: new memory limit set to 256Mi'},
    {'id':'run1','text':'Deployment deploy-111 failed during post-start hook'}
]

class Req(BaseModel):
    query: str
    context: dict = {}

@app.get('/healthz')
def health():
    return {'status':'ok'}

@app.post('/ask')
def ask(req: Req):
    tokens = req.query.lower().split()
    hits = [d for d in DOCS if any(t in d['text'].lower() for t in tokens)]
    if not hits:
        answer = 'No relevant evidence found. Check logs and traces.'
    else:
        answer = 'Likely cause: memory exhaustion (OOM). Evidence: ' + '; '.join([h['text'] for h in hits])
    recommendation = {'type':'scale','replicas':3}
    return {'answer': answer, 'recommendation': recommendation, 'sources': hits}
