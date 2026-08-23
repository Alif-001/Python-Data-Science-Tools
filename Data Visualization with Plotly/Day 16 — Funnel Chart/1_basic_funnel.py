# ======================================
# DAY 16: BASIC FUNNEL CHART
# ======================================

import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("funnel_data.csv")

# --------------------------------------
# Basic funnel visualization
# --------------------------------------

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Basic Funnel Chart"
)

fig.show()

"""
KEY IDEA:

Funnel chart shows:
✔ step-by-step reduction
✔ flow of users/customers
✔ conversion pipeline

Top = highest users
Bottom = final conversion
"""