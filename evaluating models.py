import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Dataset
data = {
    "Hours_Studied":[2,3,4,5,6,7,8,9,10,11],
    "Attendance":[60,65,70,72,75,80,85,88,90,95],
    "Result":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Hours_Studied","Attendance"]]
y = df["Result"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train,y_train)
log_pred = log_model.predict(X_test)

# Decision Tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train,y_train)
tree_pred = tree_model.predict(X_test)

# Function to print evaluation
def evaluate(name, y_test, pred):
    print("\nModel:", name)
    print("Accuracy:", accuracy_score(y_test,pred))
    print("Precision:", precision_score(y_test,pred, zero_division=0))
    print("Recall:", recall_score(y_test,pred, zero_division=0))
    print("F1 Score:", f1_score(y_test,pred, zero_division=0))

# Evaluate both models
evaluate("Logistic Regression", y_test, log_pred)
evaluate("Decision Tree", y_test, tree_pred)

print("\nComparison:")
print("The model with higher Accuracy and F1 Score is considered better.")
