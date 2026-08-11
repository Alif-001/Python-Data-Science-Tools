import pandas as pd

"""
INSIGHT GENERATION (TEXT SUMMARY)
---------------------------------
EDA is not only plots — also insights.
"""

df = pd.read_csv("eda_data.csv")

print("===== DATA INSIGHTS =====")

print("\n1. Average Salary:", df["salary"].mean())
print("2. Max Salary:", df["salary"].max())
print("3. Min Salary:", df["salary"].min())

print("\n4. Average Experience:", df["experience"].mean())
print("5. Most Common Department:", df["department"].mode()[0])

print("\n6. Correlation (Salary vs Experience):")
print(df[["salary", "experience"]].corr())