"""Train simple per-test classifiers on synthetic data."""
import numpy as np, joblib, os
from sklearn.ensemble import GradientBoostingClassifier

def make_data(num_tests=30, samples=2000):
    rng = np.random.RandomState(0)
    X = rng.randint(0,2,size=(samples, num_tests))
    y = rng.binomial(1, 0.12, size=(samples, num_tests))
    return X,y

if __name__ == '__main__':
    X,y = make_data()
    os.makedirs('models', exist_ok=True)
    models = {}
    for i in range(X.shape[1]):
        clf = GradientBoostingClassifier(n_estimators=50, random_state=42)
        clf.fit(X, y[:,i])
        models[f'test_{i}'] = clf
    joblib.dump(models, 'models/test_prio_models.joblib')
    print('Saved test prioritizer models')
