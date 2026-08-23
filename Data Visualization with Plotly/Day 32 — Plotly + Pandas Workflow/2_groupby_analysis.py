# ======================================
# GROUPBY ANALYSIS WITH PANDAS + PLOTLY
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("ecommerce_data.csv")

# --------------------------------------
# GROUP BY CATEGORY
# --------------------------------------

category_sales = df.groupby("category")["sales"].sum().reset_index()

print(category_sales)

# --------------------------------------
# Visualization: Category-wise sales
# --------------------------------------

fig = px.bar(
    category_sales,
    x="category",
    y="sales",
    color="category",
    title="Total Sales by Category"
)

fig.show()

"""
KEY IDEA:

groupby() helps to:
✔ summarize data
✔ find insights
✔ reduce complexity

This is core of EDA
"""