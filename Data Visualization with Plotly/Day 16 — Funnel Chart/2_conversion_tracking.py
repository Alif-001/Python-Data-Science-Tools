# ======================================
# CONVERSION TRACKING FUNNEL
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

# --------------------------------------
# Calculate conversion percentage
# --------------------------------------

df["conversion_rate"] = df["value"] / df["value"].iloc[0] * 100

print(df)

# --------------------------------------
# Funnel chart
# --------------------------------------

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Conversion Funnel Tracking"
)

fig.show()

"""
KEY IDEA:

Conversion rate tells:
✔ how many users move to next stage
✔ where drop-offs happen

Example:
Visitors → Signups = 50% conversion
"""