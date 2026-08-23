# ======================================
# LIVE DATA SIMULATION
# ======================================

import plotly.graph_objects as go
import random
import time

fig = go.Figure()

x_data = []
y_data = []

fig.add_trace(go.Scatter(x=x_data, y=y_data, mode="lines+markers"))

fig.show()

# --------------------------------------
# Simulate real-time data stream
# --------------------------------------

for i in range(20):

    x_data.append(i)

    # random live value (like stock price)
    new_value = random.randint(100, 300)
    y_data.append(new_value)

    # update chart
    fig.data[0].x = x_data
    fig.data[0].y = y_data

    print(f"New value: {new_value}")

    time.sleep(1)

"""
KEY IDEA:

✔ simulates stock market
✔ real-time random updates
✔ dynamic visualization concept
"""