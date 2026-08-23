# ======================================
# ADVANCED DASHBOARD STYLING
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Line chart for dashboard
# --------------------------------------

fig = px.line(df, x="month", y="sales", markers=True)

# --------------------------------------
# FULL dashboard styling
# --------------------------------------

fig.update_layout(
    title="📈 Advanced Sales Dashboard",

    # background styling
    plot_bgcolor="lightgray",
    paper_bgcolor="white",

    # margin control
    margin=dict(l=40, r=40, t=60, b=40),

    # axis styling
    xaxis=dict(
        showgrid=False,
        title="Month"
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="white",
        title="Sales"
    ),

    # font customization
    font=dict(
        family="Verdana",
        size=14,
        color="black"
    )
)

fig.show()

"""
KEY IDEA:

Advanced layout controls:
✔ background colors
✔ margins (spacing)
✔ grid control
✔ professional dashboard design

This is used in real BI dashboards
"""