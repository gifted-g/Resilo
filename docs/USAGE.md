# USAGE.md - Resilo (How to use the POC)

## Dashboard
- Open http://localhost:3000/deployments
- The AI Assistant widget lets you ask about a deployment (it will call the AI assistant backend)

## AI endpoints (examples)
Predictive service:
```
POST http://localhost:8080/predict
{
  "test_fail_rate": 0.5,
  "cpu_slope": 0.1,
  "files_changed": 3,
  "deploy_frequency": 0.2
}
```
Root-cause service:
```
POST http://localhost:8081/root_cause
{
  "mem_pct": 85.0,
  "cpu_pct": 70.0,
  "error_rate": 5.0,
  "recent_config_change": 1
}
```

Test prioritizer:
```
POST http://localhost:8082/prioritize
{ "changed_files_vector": [1,0,0,1,...] }
```

AI assistant:
```
POST http://localhost:8083/ask
{ "query": "Why did deploy-111 fail?", "context":{"deploymentId":"deploy-111"} }
```

## Notes
- The AI models are simple scikit-learn models trained on synthetic data to be runnable out-of-the-box.
- For production, swap to real data, add model registry (MLflow/BentoML), secure endpoints (mTLS/JWT), monitoring.
