# ======================================
# ADVANCED SUNBURST CUSTOMIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Advanced sunburst styling
# --------------------------------------

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="department",
    title="Advanced Sunburst Chart"
)

# Improve layout spacing
fig.update_layout(
    margin=dict(t=40, l=0, r=0, b=0)
)

fig.show()

"""
KEY IDEA:

Sunburst chart is best for:
✔ hierarchical analysis
✔ multi-level breakdown
✔ circular visualization style

Very common in dashboards
"""