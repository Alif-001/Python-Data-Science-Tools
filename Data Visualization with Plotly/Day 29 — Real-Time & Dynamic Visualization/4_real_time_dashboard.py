# ======================================
# REAL-TIME DASHBOARD SIMULATION
# ======================================

import plotly.graph_objects as go
import random
import time

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

x_data = []
y_data = []

fig.add_trace(go.Scatter(
    x=x_data,
    y=y_data,
    mode="lines",
    name="Live Sales"
))

fig.update_layout(
    title="Real-Time Dashboard Simulation",
    xaxis_title="Time",
    yaxis_title="Sales Value"
)

fig.show()

# --------------------------------------
# Real-time update loop
# --------------------------------------

for t in range(50):

    x_data.append(t)

    # simulate real business metric
    sales = random.randint(80, 400)
    y_data.append(sales)

    # update chart
    fig.data[0].x = x_data
    fig.data[0].y = y_data

    # print dashboard log
    print(f"Time {t} → Sales: {sales}")

    time.sleep(0.3)

"""
KEY IDEA:

This simulates:
✔ live business dashboard
✔ continuously updating KPIs
✔ real-world monitoring systems

Used in:
- stock markets
- IoT dashboards
- business analytics
"""