# ======================================
# BUSINESS BREAKDOWN TREEMAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Add color for deeper insight
# --------------------------------------

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="revenue",   # color intensity
    title="Business Revenue Breakdown"
)

fig.show()

"""
KEY IDEA:

color=
→ adds visual intensity

Darker/larger blocks = higher revenue

This is very useful in:
✔ business dashboards
✔ KPI tracking
"""