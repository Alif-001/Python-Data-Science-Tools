# ======================================
# DAY 33: RANDOM SIMULATION VISUALIZATION
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Simulate random walk (like stock price)
# --------------------------------------

np.random.seed(42)

steps = 100
x = np.arange(steps)

# start value
price = 100
prices = []

for _ in range(steps):

    # random change (-2 to +2)
    change = np.random.randint(-2, 3)
    price += change
    prices.append(price)

# --------------------------------------
# Plot simulation
# --------------------------------------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=prices,
    mode="lines+markers",
    name="Stock Simulation"
))

fig.update_layout(
    title="Random Walk Simulation (Stock-like)",
    xaxis_title="Time",
    yaxis_title="Price"
)

fig.show()

"""
KEY IDEA:

✔ randomness creates patterns
✔ used in finance simulation
✔ stock market modeling
"""