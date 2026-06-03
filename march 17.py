import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

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
    ("model", DecisionTreeClassifier(max_depth=3))
])

pipe.fit(X_train, y_train)

pred = pipe.predict(X_test)

plt.scatter(X_test["Hours_Studied"], pred)
plt.xlabel("Hours Studied")
plt.ylabel("Predicted Pass")
plt.title("Prediction vs Study Hours")
plt.show()

plt.scatter(X_test["Sleep_Hours"], pred)
plt.xlabel("Sleep Hours")
plt.ylabel("Predicted Pass")
plt.title("Prediction vs Sleep Hours")
plt.show()