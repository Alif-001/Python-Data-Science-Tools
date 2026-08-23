# ======================================
# ANIMATED BAR CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("yearly_sales.csv")

# --------------------------------------
# Animated bar chart
# --------------------------------------

fig = px.bar(
    df,
    x="country",
    y="sales",

    # animate by year
    animation_frame="year",

    # color bars
    color="country",

    title="Animated Sales Comparison"
)

fig.show()

"""
KEY IDEA:

Animated bar chart helps:
✔ compare growth over time
✔ track rankings dynamically
✔ show changing performance

Very popular in business dashboards
"""