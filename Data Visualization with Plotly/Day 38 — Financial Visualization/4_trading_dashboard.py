# ======================================
# DAY 38: TRADING DASHBOARD (BASIC)
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("stock_data.csv")

# --------------------------------------
# Moving average (trend indicator)
# --------------------------------------

df["MA3"] = df["close"].rolling(window=3).mean()

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# Close price
fig.add_trace(go.Scatter(
    x=df["date"],
    y=df["close"],
    mode="lines+markers",
    name="Close Price"
))

# Moving average
fig.add_trace(go.Scatter(
    x=df["date"],
    y=df["MA3"],
    mode="lines",
    name="Moving Average (3-day)"
))

fig.update_layout(
    title="Trading Dashboard (Price + Trend)",
    xaxis_title="Date",
    yaxis_title="Price"
)

fig.show()

"""
KEY IDEA:

✔ moving average = trend smoothing
✔ helps detect market direction
✔ used in trading strategies
"""