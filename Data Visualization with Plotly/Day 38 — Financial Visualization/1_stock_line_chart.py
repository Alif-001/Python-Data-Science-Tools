# ======================================
# DAY 38: STOCK LINE CHART
# ======================================

import pandas as pd
import plotly.graph_objects as go

# Load stock data
df = pd.read_csv("stock_data.csv")

# --------------------------------------
# Simple stock price visualization
# --------------------------------------

fig = go.Figure()

# Closing price line chart
fig.add_trace(go.Scatter(
    x=df["date"],
    y=df["close"],
    mode="lines+markers",
    name="Close Price"
))

fig.update_layout(
    title="Stock Closing Price Trend",
    xaxis_title="Date",
    yaxis_title="Price"
)

fig.show()

"""
KEY IDEA:

✔ simple stock trend
✔ shows price movement over time
"""