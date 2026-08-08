import pandas as pd

df = pd.read_csv("data/cognifact_machine_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)
print("\nDataset shape:")
print(df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic statistics:")
print(df.describe())