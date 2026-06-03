import numpy as np
import pandas as pd


arr = np.array([5, 10, 15, 20, 25])

print("First element:", arr[0])
print("Last element:", arr[-1])

print("Elements from index 1 to 3:", arr[1:4])

print("Elements greater than 15:", arr[arr > 15])


data = {
    "Name": ["amrita", "kiran", "siva", "kumar"],
    "Age": [22, 25, 23, 30],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("\nNames column:")
print(df["Name"])

print("\nStudents with Marks > 85:")
print(df[df["Marks"] > 85])


print("\nUsing loc (row 1):")
print(df.loc[1])


print("\nUsing iloc (row 2, column 1):")
print(df.iloc[2, 1])