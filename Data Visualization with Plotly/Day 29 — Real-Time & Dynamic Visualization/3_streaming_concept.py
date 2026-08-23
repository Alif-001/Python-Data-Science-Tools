# ======================================
# STREAMING CONCEPT (REAL DASHBOARD IDEA)
# ======================================

import plotly.graph_objects as go
import time
import random

fig = go.Figure()

x_data = []
y_data = []

fig.add_trace(go.Scatter(
    x=x_data,
    y=y_data,
    mode="lines+markers",
    name="Live Stream"
))

fig.show()

# --------------------------------------
# Streaming simulation loop
# --------------------------------------

for i in range(30):

    # simulate incoming data packet
    x_data.append(i)
    y_data.append(random.randint(50, 500))

    # keep only last 10 points (real dashboard behavior)
    x_data = x_data[-10:]
    y_data = y_data[-10:]

    fig.data[0].x = x_data
    fig.data[0].y = y_data

    time.sleep(0.5)

"""
KEY IDEA:

Streaming dashboards:
✔ show only recent data
✔ remove old values
✔ simulate live feed systems
"""