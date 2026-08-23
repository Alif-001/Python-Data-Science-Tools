# ======================================
# DONUT CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

# --------------------------------------
# Create donut chart
# --------------------------------------

fig = px.pie(
    df,
    names="brand",
    values="sales",
    hole=0.4,   # creates donut hole
    title="Donut Chart: Market Share"
)

fig.show()

"""
KEY IDEA:

hole=
→ converts pie chart into donut chart

Why use donut chart?
✔ cleaner look
✔ modern dashboard style
✔ space for center text
"""