# ======================================
# STACKED AREA CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------
# Stacked area chart by product
# --------------------------------------

fig = px.area(
    df,
    x="date",
    y="sales",
    color="product",   # stacking by category
    title="Stacked Area Chart: Product-wise Sales"
)

fig.show()

"""
KEY IDEA:

color=
→ creates stacked groups

Stacked area chart helps:
✔ compare categories over time
✔ see contribution of each product
✔ total + breakdown analysis
"""