# ======================================
# DAY 39: SIMULATION MODEL (POPULATION GROWTH)
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Time steps
# --------------------------------------

t = np.arange(0, 50)

# --------------------------------------
# Logistic growth model (scientific simulation)
# --------------------------------------

K = 100  # carrying capacity
P0 = 5   # initial population
r = 0.2  # growth rate

population = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# --------------------------------------
# Plot simulation
# --------------------------------------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=t,
    y=population,
    mode="lines",
    name="Population Growth"
))

fig.update_layout(
    title="Simulation: Logistic Growth Model",
    xaxis_title="Time",
    yaxis_title="Population"
)

fig.show()

"""
KEY IDEA:

✔ models real biological growth
✔ used in ecology + AI modeling
"""