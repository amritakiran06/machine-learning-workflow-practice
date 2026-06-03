import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

data = {
    "Experience": [1, 3, 5, np.nan, 2],
    "Income": [20000, np.nan, 50000, 60000, 30000],
    "Department": ["HR", "IT", np.nan, "Finance", "IT"]
}

df = pd.DataFrame(data)

print("Initial Data:\n", df)

num_features = ["Experience", "Income"]
num_fill = SimpleImputer(strategy="median")
df[num_features] = num_fill.fit_transform(df[num_features])

df["Department"] = df["Department"].fillna("Unknown")

print("\nAfter Filling Missing Values:\n", df)

encoder = OneHotEncoder(sparse_output=False)
dept_encoded = encoder.fit_transform(df[["Department"]])

dept_df = pd.DataFrame(
    dept_encoded,
    columns=encoder.get_feature_names_out(["Department"])
)

df = pd.concat([df.drop("Department", axis=1), dept_df], axis=1)

print("\nAfter Encoding:\n", df)

scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)

df_final = pd.DataFrame(scaled_values, columns=df.columns)

print("\nFinal Scaled Data:\n", df_final)