# ======================================
# FULL EDA DASHBOARD (BEGINNER VERSION)
# ======================================

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("ecommerce_data.csv")

# --------------------------------------
# Create summary tables using groupby
# --------------------------------------

region_sales = df.groupby("region")["sales"].sum().reset_index()
category_profit = df.groupby("category")["profit"].sum().reset_index()

# --------------------------------------
# Create dashboard layout
# --------------------------------------

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Sales by Region", "Profit by Category")
)

# --------------------------------------
# Region Sales Chart
# --------------------------------------

fig.add_trace(
    go.Bar(
        x=region_sales["region"],
        y=region_sales["sales"],
        name="Region Sales"
    ),
    row=1, col=1
)

# --------------------------------------
# Category Profit Chart
# --------------------------------------

fig.add_trace(
    go.Bar(
        x=category_profit["category"],
        y=category_profit["profit"],
        name="Category Profit"
    ),
    row=1, col=2
)

fig.update_layout(
    title="📊 EDA Dashboard - E-commerce Data",
    showlegend=False
)

fig.show()

"""
KEY IDEA:

EDA Dashboard shows:
✔ sales insights
✔ profit insights
✔ grouped analysis

This is real data analysis workflow
"""