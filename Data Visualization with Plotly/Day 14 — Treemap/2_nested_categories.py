# ======================================
# NESTED CATEGORIES TREEMAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Multi-level hierarchy
# --------------------------------------

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    title="Nested Hierarchy Treemap"
)

fig.show()

"""
KEY IDEA:

path=
→ defines hierarchy levels

Here:
company → department → team

This helps understand:
✔ structure of organization
✔ revenue breakdown
"""