# ======================================
# DAY 9: BASIC PIE CHART
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("market_share.csv")

print(df)

# --------------------------------------
# Basic pie chart
# --------------------------------------

fig = px.pie(
    df,
    names="brand",   # category labels
    values="sales",  # numeric values
    title="Smartphone Market Share"
)

fig.show()

"""
KEY IDEA:

Pie chart shows:
✔ proportions
✔ percentage share
✔ part-to-whole relationship

Example:
- market share
- budget allocation
- vote percentage
"""