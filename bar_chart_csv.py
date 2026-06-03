import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.figure()

plt.bar(df["Month"], df["Profit"])

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.show()