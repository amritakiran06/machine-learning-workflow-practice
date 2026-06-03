import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()

model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

prediction = model.predict([[6]])
print("Prediction for x=6:", prediction)