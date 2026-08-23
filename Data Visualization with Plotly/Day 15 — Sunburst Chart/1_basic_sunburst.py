# ======================================
# DAY 15: BASIC SUNBURST CHART
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("company_data.csv")

# --------------------------------------
# Basic Sunburst Chart
# --------------------------------------

fig = px.sunburst(
    df,
    path=["company", "department"],
    values="revenue",
    title="Company → Department Revenue (Sunburst)"
)

fig.show()

"""
KEY IDEA:

Sunburst chart shows:
✔ hierarchy in circular form
✔ inner circle = parent
✔ outer rings = children

Example:
TechCorp → Engineering → Revenue breakdown
"""