import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.plot(df["Month"], df["Sales"], marker='o', label="Sales")
plt.plot(df["Month"], df["Profit"], marker='s', label="Profit")

plt.title("Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.show()