# ======================================
# DAY 38: OHLC CHART
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("stock_data.csv")

# --------------------------------------
# OHLC chart (Open-High-Low-Close)
# --------------------------------------

fig = go.Figure(data=[go.Ohlc(

    x=df["date"],
    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"]

)])

fig.update_layout(
    title="OHLC Chart (Trading View Style)",
    xaxis_title="Date",
    yaxis_title="Price"
)

fig.show()

"""
KEY IDEA:

OHLC chart = simplified candlestick view

✔ used in finance analysis tools
"""