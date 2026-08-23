# ======================================
# INTERACTIVE FEATURES
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales.csv")

# --------------------------------------
# Hover tooltips + interactivity
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    color="region",
    size="sales",
    hover_data=["day", "region"],
    title="Sales vs Profit (Interactive)"
)

# --------------------------------------
# Hover customization
# --------------------------------------
fig.update_traces(
    hovertemplate=
    "Sales: %{x}<br>" +
    "Profit: %{y}<br>" +
    "<extra></extra>"
)

# --------------------------------------
# Zoom & Pan is automatic in Plotly
# --------------------------------------
# You can:
# - scroll to zoom
# - drag to pan
# - hover for details

fig.show()

"""
KEY IDEA:

Plotly is interactive by default:
✔ Zoom
✔ Pan
✔ Hover tooltips
✔ Click legends
"""