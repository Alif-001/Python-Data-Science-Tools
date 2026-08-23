# ======================================
# DAY 29: BASIC DYNAMIC UPDATE
# ======================================

import plotly.graph_objects as go
import time

# --------------------------------------
# Create initial figure
# --------------------------------------

fig = go.Figure()

# Start empty data
x_data = []
y_data = []

fig.add_trace(go.Scatter(x=x_data, y=y_data, mode="lines+markers"))

fig.show()

# --------------------------------------
# Simulate live updates
# --------------------------------------

for i in range(10):
    x_data.append(i)
    y_data.append(i * 10)

    # update chart dynamically
    fig.data[0].x = x_data
    fig.data[0].y = y_data

    time.sleep(1)

"""
KEY IDEA:

✔ chart updates step-by-step
✔ simulates live data
✔ foundation of real dashboards
"""