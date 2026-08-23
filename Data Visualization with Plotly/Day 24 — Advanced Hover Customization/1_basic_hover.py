# ======================================
# DAY 24: BASIC HOVER CUSTOMIZATION
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("company_sales.csv")

# --------------------------------------
# Basic scatter plot with hover
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    # hover label
    hover_name="company",

    title="Basic Hover Information"
)

fig.show()

"""
KEY IDEA:

Hover shows:
✔ extra information
✔ interactive details
✔ cleaner visualization

Move mouse over points to see tooltip
"""