# ======================================
# DAY 14: BASIC TREEMAP
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("company_data.csv")

# --------------------------------------
# Basic treemap (single hierarchy level)
# --------------------------------------

fig = px.treemap(
    df,
    path=["company", "department"],
    values="revenue",
    title="Company Revenue Treemap"
)

fig.show()

"""
KEY IDEA:

Treemap shows:
✔ hierarchical structure
✔ contribution of each category
✔ part-to-whole relationship

Bigger boxes = more revenue
"""