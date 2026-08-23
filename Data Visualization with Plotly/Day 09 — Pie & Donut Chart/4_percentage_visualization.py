# ======================================
# PERCENTAGE VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

# --------------------------------------
# Pie chart with percentages
# --------------------------------------

fig = px.pie(
    df,
    names="brand",
    values="sales",
    title="Percentage Visualization"
)

# Customize percentage display
fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

fig.show()

"""
KEY IDEA:

Pie charts are excellent for:
✔ percentage understanding
✔ contribution analysis
✔ quick summary visualization
"""