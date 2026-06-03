import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,2,3,4],
    "Sleep_Hours":  [7,6,6,5,5,4,4,3,3,7,6,5],
    "Pass":         [0,0,0,1,1,1,1,1,1,0,0,1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Sleep_Hours"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

pipe = Pipeline([
    ("imputer", SimpleImputer()),
    ("scaler", StandardScaler()),
    ("model", DecisionTreeClassifier())
])

params = {
    "model__max_depth": [2, 3, 4],
    "model__min_samples_split": [2, 3]
}

grid = GridSearchCV(pipe, params, cv=2)

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

pred = best_model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("Best Parameters:", grid.best_params_)
print("Accuracy:", acc)