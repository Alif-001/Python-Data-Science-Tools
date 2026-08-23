# ======================================
# GROUPED BAR CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Grouped bar chart
# --------------------------------------

fig = px.bar(
    df,
    x="month",
    y="sales",
    color="region",   # creates groups
    barmode="group",
    title="Grouped Bar Chart: Sales by Region"
)

fig.show()

"""
KEY IDEA:

barmode="group"

→ puts bars side by side

Useful for:
✔ comparing categories
✔ region comparison
✔ performance analysis
"""