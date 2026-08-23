# ======================================
# ADVANCED TREEMAP CUSTOMIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Advanced styling
# --------------------------------------

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="department",
    title="Advanced Treemap with Styling"
)

# Improve layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()

"""
KEY IDEA:

Treemap is useful for:
✔ hierarchy visualization
✔ business structure analysis
✔ resource distribution

This is commonly used in dashboards
"""