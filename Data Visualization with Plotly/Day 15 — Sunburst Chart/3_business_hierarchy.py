# ======================================
# BUSINESS HIERARCHY ANALYSIS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Add color for deeper insight
# --------------------------------------

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="revenue",
    title="Business Hierarchy with Revenue Intensity"
)

fig.show()

"""
KEY IDEA:

color=
→ shows intensity of values

Darker/larger segments = higher revenue

Useful for:
✔ business dashboards
✔ KPI analysis
"""