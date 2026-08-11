import pandas as pd

"""
DAY 32 - EDA VISUALIZATION PROJECT
----------------------------------
Step 1: Load and understand data
"""

# Load dataset
df = pd.read_csv("eda_data.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Basic info about dataset
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())