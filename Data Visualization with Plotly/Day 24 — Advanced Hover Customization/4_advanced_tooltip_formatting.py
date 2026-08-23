# ======================================
# ADVANCED TOOLTIP FORMATTING
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_sales.csv")

# --------------------------------------
# Advanced interactive chart
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    size="employees",
    color="company",

    hover_name="company",

    hover_data={
        "year": True,

        # format numeric values
        "sales": ":,.0f",
        "profit": ":,.0f",

        # hide employee column
        "employees": False
    },

    title="Advanced Tooltip Formatting"
)

fig.show()

"""
KEY IDEA:

hover_data formatting:
✔ cleaner numbers
✔ readable tooltips
✔ selective information display

This is professional dashboard design
"""