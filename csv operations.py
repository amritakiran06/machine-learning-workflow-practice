import pandas as pd

df = pd.read_csv("file.csv")

print("Full Dataset:")
print(df)

print("\nSelecting Single Column (Marks):")
print(df["Marks"])

print("\nSelecting Multiple Columns (Name and Marks):")
print(df[["Name", "Marks"]])

print("\nStudents with Marks > 80:")
high_scorers = df[df["Marks"] > 80]
print(high_scorers)

print("\nStudents with Age >= 23:")
age_filter = df[df["Age"] >= 23]
print(age_filter)

print("\nAverage Marks:", df["Marks"].mean())
print("Total Marks:", df["Marks"].sum())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())
print("Count of Students:", df["Name"].count())