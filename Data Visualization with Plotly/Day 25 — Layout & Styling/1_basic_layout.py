# ======================================
# DAY 25: BASIC LAYOUT CONTROL
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Basic line chart
# --------------------------------------

fig = px.line(df, x="month", y="sales", title="Basic Sales Chart")

# --------------------------------------
# update_layout() controls overall design
# --------------------------------------

fig.update_layout(
    title="Updated Layout Example"
)

fig.show()

"""
KEY IDEA:

update_layout():
✔ controls full figure design
✔ modifies title, margins, background
✔ improves UI quality
"""