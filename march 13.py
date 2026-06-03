import pandas as pd

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Sleep_Hours": [7, 6, 6, 5, 5, 4, 4],
    "Pass": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Sleep_Hours"]]
y = df["Pass"]

print("Dataset:\n", df)
print("\nProblem: Predict student pass/fail based on study and sleep hours")
print("\nFeatures:\n", X.head())
print("\nTarget:\n", y.head())