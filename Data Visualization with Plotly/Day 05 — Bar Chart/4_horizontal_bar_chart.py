# ======================================
# HORIZONTAL BAR CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Calculate total sales by region
# --------------------------------------

region_sales = df.groupby("region")["sales"].sum().reset_index()

print(region_sales)

# --------------------------------------
# Horizontal bar chart
# --------------------------------------

fig = px.bar(
    region_sales,
    x="sales",
    y="region",
    orientation="h",   # horizontal mode
    color="sales",
    title="Total Sales by Region"
)

fig.show()

"""
KEY IDEA:

orientation="h"

→ makes horizontal bars

Best for:
✔ long category names
✔ ranking charts
✔ readability
"""