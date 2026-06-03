import pandas as pd

data = {
    "Name": ["kiran", "amrita", "rahul"],
    "Age": [22, 25, 23],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nFirst 2 rows:")
print(df.head(2))

print("\nColumn Names:", df.columns)
print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())