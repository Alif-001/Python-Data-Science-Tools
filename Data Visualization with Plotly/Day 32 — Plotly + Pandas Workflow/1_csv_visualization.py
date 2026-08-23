# ======================================
# DAY 32: BASIC CSV VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load CSV file (real-world workflow)
# --------------------------------------

df = pd.read_csv("ecommerce_data.csv")

# --------------------------------------
# Quick look at data
# --------------------------------------

print(df.head())

# --------------------------------------
# Simple visualization: Sales per product
# --------------------------------------

fig = px.bar(
    df,
    x="product",
    y="sales",
    color="category",
    title="Sales by Product"
)

fig.show()

"""
KEY IDEA:

CSV → DataFrame → Visualization

✔ most common workflow in data science
✔ used in every analytics project
"""