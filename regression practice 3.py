import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([30000,35000,40000,45000,50000,55000,60000,65000,70000,75000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Test Inputs:", X_test)
print("Predicted Salaries:", y_pred)
print("Actual Salaries:", y_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

prediction = model.predict([[12]])
print("Predicted salary for 12 years experience:", prediction)