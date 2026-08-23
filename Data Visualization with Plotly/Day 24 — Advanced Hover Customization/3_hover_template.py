# ======================================
# HOVER TEMPLATE CUSTOMIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_sales.csv")

# --------------------------------------
# Create scatter plot
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    color="company",
    title="Hover Template Example"
)

# --------------------------------------
# Custom hover template
# --------------------------------------

fig.update_traces(
    hovertemplate=
    "<b>Company:</b> %{marker.color}<br>" +
    "<b>Sales:</b> %{x} Million<br>" +
    "<b>Profit:</b> %{y} Million<br>" +
    "<extra></extra>"
)

fig.show()

"""
KEY IDEA:

hovertemplate=
✔ fully custom tooltip
✔ professional formatting
✔ complete control

<extra></extra>
removes default secondary box
"""