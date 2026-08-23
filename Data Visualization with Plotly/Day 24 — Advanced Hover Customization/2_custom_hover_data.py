# ======================================
# CUSTOM HOVER DATA
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_sales.csv")

# --------------------------------------
# Add custom hover fields
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    hover_name="company",

    # extra hover information
    hover_data=[
        "year",
        "employees"
    ],

    title="Custom Hover Data Example"
)

fig.show()

"""
KEY IDEA:

hover_data=
✔ adds more information
✔ improves interactivity
✔ creates rich tooltips

Very useful in dashboards
"""