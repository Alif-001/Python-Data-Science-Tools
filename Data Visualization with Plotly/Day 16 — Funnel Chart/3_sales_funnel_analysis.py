# ======================================
# SALES FUNNEL ANALYSIS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

# --------------------------------------
# Enhanced funnel with color
# --------------------------------------

fig = px.funnel(
    df,
    x="value",
    y="stage",
    color="value",
    title="Sales Funnel Analysis"
)

fig.show()

"""
KEY IDEA:

Color helps visualize:
✔ intensity of each stage
✔ drop-off rate
✔ performance strength

Used in:
✔ marketing analytics
✔ sales dashboards
"""