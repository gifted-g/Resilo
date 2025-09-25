"""Train a simple GradientBoosting model for failure risk using synthetic data."""
import numpy as np, joblib, os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report

def make_data(n=5000):
    rng = np.random.RandomState(42)
    # features: test_fail_rate, cpu_slope, files_changed, deploy_frequency
    X = rng.normal(loc=0.0, scale=1.0, size=(n,4))
    # construct a risk
    risk = 0.8*X[:,0] + 0.5*X[:,1] + 0.3*(X[:,2]>0).astype(float)
    prob = 1/(1+np.exp(-risk))
    y = (prob > 0.6).astype(int)
    return X,y

if __name__ == '__main__':
    X,y = make_data(5000)
    X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2, random_state=42)
    clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train,y_train)
    preds = clf.predict_proba(X_val)[:,1]
    auc = roc_auc_score(y_val, preds)
    print('AUC:', auc)
    os.makedirs('models', exist_ok=True)
    joblib.dump({'model':clf, 'features':['test_fail_rate','cpu_slope','files_changed','deploy_frequency']}, 'models/predict_failure.joblib')
    print('Model saved: models/predict_failure.joblib')
