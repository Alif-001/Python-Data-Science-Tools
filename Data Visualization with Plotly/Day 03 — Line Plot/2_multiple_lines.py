# ======================================
# MULTIPLE LINES IN ONE CHART
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------
# Multiple lines using "melt style approach"
# --------------------------------------

df_melted = df.melt(
    id_vars="date",
    value_vars=["sales", "profit"],
    var_name="metric",
    value_name="value"
)

# --------------------------------------
# Plot multiple lines
# --------------------------------------
fig = px.line(
    df_melted,
    x="date",
    y="value",
    color="metric",   # creates multiple lines
    title="Sales vs Profit Trend"
)

fig.show()

"""
KEY IDEA:

color="metric"
→ automatically creates multiple lines

This is very important for dashboards.
"""