import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Sleep_Hours": [7, 6, 6, 5, 5, 4, 4],
    "Pass": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Sleep_Hours"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Test Inputs:\n", X_test)
print("\nPredictions:", predictions)
print("\nActual:", y_test.values)