import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from sklearn.tree import DecisionTreeClassifier

data = {
    "Attendance": [65, 70, np.nan, 80, 90, np.nan, 85],
    "Assignments": [50, 60, 55, np.nan, 75, 80, 70],
    "Pass": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Attendance", "Assignments"]]
y = df["Pass"]

pipe = Pipeline([
    ("impute", KNNImputer(n_neighbors=2)),
    ("scale", RobustScaler()),
    ("clf", DecisionTreeClassifier(max_depth=3))
])

pipe.fit(X, y)

test = pd.DataFrame({
    "Attendance": [75, 85, 60],
    "Assignments": [65, 70, 55]
})

pred = pipe.predict(test)
prob = pipe.predict_proba(test)

for i in range(len(test)):
    print(f"Input: {test.iloc[i].to_dict()}")
    print(f"Predicted Class: {pred[i]}")
    print(f"Confidence: {max(prob[i]):.2f}")
    print("---")