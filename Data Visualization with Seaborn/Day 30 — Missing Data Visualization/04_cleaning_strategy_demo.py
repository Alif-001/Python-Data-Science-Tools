# 04_cleaning_strategy_demo.py

import pandas as pd

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# OPTION 1: DROP MISSING VALUES

# --------------------------------------------

df_drop = df.dropna()

print("After dropping missing values:")
print(df_drop)

# --------------------------------------------

# OPTION 2: FILL MISSING VALUES

# --------------------------------------------

df_fill = df.fillna(df.mean(numeric_only=True))

print("\nAfter filling missing values:")
print(df_fill)

# --------------------------------------------

# IDEA:

# - drop = remove data

# - fill = keep data

# --------------------------------------------
