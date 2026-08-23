# ======================================
# THEMES & STYLE CUSTOMIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create chart with template
# --------------------------------------

fig = px.bar(
    df,
    x="month",
    y="sales",
    title="Themed Bar Chart",
    template="plotly_dark"  # built-in theme
)

fig.show()

"""
KEY IDEA:

Plotly themes:
✔ plotly
✔ plotly_dark
✔ ggplot2
✔ seaborn
✔ simple_white

Themes instantly change UI style
"""