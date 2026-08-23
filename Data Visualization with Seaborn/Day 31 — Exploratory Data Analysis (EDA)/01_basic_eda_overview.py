# 01_basic_eda_overview.py

# --------------------------------------------

# DAY 31: COMPLETE EDA WORKFLOW

# --------------------------------------------

import pandas as pd

# Load dataset

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# BASIC INFORMATION

# --------------------------------------------

print(df.head())        # first rows
print(df.info())        # structure
print(df.describe())    # statistics

# --------------------------------------------

# IDEA:

# - understand dataset before plotting

# --------------------------------------------
