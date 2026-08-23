# ======================================
# TITLES + AXIS + FONTS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.line(df, x="month", y="sales")

# --------------------------------------
# Customize layout
# --------------------------------------

fig.update_layout(
    title={
        "text": "📊 Monthly Sales Report",
        "x": 0.5,   # center title
        "font": dict(size=22, color="darkblue")
    },

    xaxis_title="Months",
    yaxis_title="Sales (USD)",

    font=dict(
        family="Arial",
        size=14,
        color="black"
    )
)

fig.show()

"""
KEY IDEA:

Here we control:
✔ title position
✔ axis labels
✔ font styling

This makes charts look professional
"""