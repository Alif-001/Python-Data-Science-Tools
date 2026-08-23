# 01_sales_overview.py

# --------------------------------------------

# DAY 32: BUSINESS ANALYTICS VISUALIZATION

# --------------------------------------------

import pandas as pd

df = pd.read_csv("business_sales.csv")

# --------------------------------------------

# BASIC BUSINESS SUMMARY

# --------------------------------------------

print("Total Sales:", df["sales"].sum())
print("Total Profit:", df["profit"].sum())
print("Total Orders:", df["orders"].sum())

print("\nRegion-wise sales:")
print(df.groupby("region")["sales"].sum())

# --------------------------------------------

# IDEA:

# - first understand KPIs

# --------------------------------------------
