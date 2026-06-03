import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.figure()

plt.plot(df["Month"], df["Sales"], marker='o', label="Sales")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()