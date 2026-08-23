# ======================================
# STACKED BAR CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Stacked bar chart
# --------------------------------------

fig = px.bar(
    df,
    x="month",
    y="sales",
    color="region",
    barmode="stack",
    title="Stacked Bar Chart: Total Sales Contribution"
)

fig.show()

"""
KEY IDEA:

barmode="stack"

→ stacks bars on top of each other

Useful for:
✔ contribution analysis
✔ total + category understanding
✔ composition analysis
"""