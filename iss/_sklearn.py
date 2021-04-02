from .o3iss import compute
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np


class IssTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, level=4):
        self.level = level

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return np.array([compute(x, self.level) for x in X])


class IssClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, level=4):
        self.level = level
        self.pipeline = Pipeline(
            [
                ("scale", StandardScaler()),
                ("iss", IssTransformer(level=level)),
                ("logit", LogisticRegression()),
            ]
        )

    def fit(self, X, y):
        return self.pipeline.fit(X, y)

    def predict(self, X):
        return self.pipeline.predict(X)
