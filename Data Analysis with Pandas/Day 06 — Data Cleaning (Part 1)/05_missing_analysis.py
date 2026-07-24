# =========================================
# Missing Data Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 total missing values per column
print("Missing values per column:")
print(df.isnull().sum())

# 👉 percentage of missing values
print("\nPercentage missing:")
print(df.isnull().mean() * 100)

# 👉 total missing values in dataset
print("\nTotal missing values:")
print(df.isnull().sum().sum())

# 👉 summary:
# analysis = cleaning শুরু করার আগে বোঝা জরুরি