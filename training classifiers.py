import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Hours_Studied": [2, 3, 5, 6, 8, 9],
    "Attendance": [60, 65, 70, 80, 85, 90],
    "Result": [0, 0, 0, 1, 1, 1]  
}
df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

prediction = model.predict([[7, 75]])

print("Prediction (0=Fail, 1=Pass):", prediction)