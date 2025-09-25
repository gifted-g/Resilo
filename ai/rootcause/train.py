"""Train a simple multi-class root-cause classifier on synthetic data."""
import numpy as np, joblib, os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def make_data(n=3000):
    rng = np.random.RandomState(1)
    X = rng.normal(size=(n,3))
    rc = rng.binomial(1, 0.2, size=(n,1))
    X = np.hstack([X, rc])
    y = rng.choice([0,1,2,3], size=n, p=[0.25,0.25,0.25,0.25])
    return X,y

if __name__ == '__main__':
    X,y = make_data(4000)
    Xtr,Xv,ytr,yv = train_test_split(X,y,test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(Xtr,ytr)
    print('Train done')
    os.makedirs('models', exist_ok=True)
    joblib.dump({'model':clf, 'features':['mem_pct','cpu_pct','error_rate','recent_config_change']}, 'models/root_cause.joblib')
    print('Saved root cause model')
