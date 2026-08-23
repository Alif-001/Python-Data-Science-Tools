# ======================================
# DAY 38: CANDLESTICK CHART (IMPORTANT)
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("stock_data.csv")

# --------------------------------------
# Candlestick chart (OHLC visualization)
# --------------------------------------

fig = go.Figure(data=[go.Candlestick(

    x=df["date"],

    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"]

)])

fig.update_layout(
    title="Candlestick Chart (Stock Movement)",
    xaxis_title="Date",
    yaxis_title="Price"
)

fig.show()

"""
KEY IDEA:

Candlestick shows:

✔ Open price
✔ High price
✔ Low price
✔ Close price

Used in real trading platforms 📊
"""