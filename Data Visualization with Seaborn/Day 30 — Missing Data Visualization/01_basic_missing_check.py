# 01_basic_missing_check.py

# --------------------------------------------

# DAY 30: MISSING DATA VISUALIZATION

# --------------------------------------------

import pandas as pd

# Load dataset

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# CHECK MISSING VALUES

# --------------------------------------------

print("Missing values per column:")
print(df.isnull().sum())

# --------------------------------------------

# IDEA:

# - shows how much data is missing

# --------------------------------------------
