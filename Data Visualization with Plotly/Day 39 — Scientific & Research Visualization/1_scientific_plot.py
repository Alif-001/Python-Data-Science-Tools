# ======================================
# DAY 39: SCIENTIFIC FUNCTION PLOT
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Create scientific x-axis (time or distance)
# --------------------------------------

x = np.linspace(0, 10, 200)

# --------------------------------------
# Physics-style function (wave simulation)
# --------------------------------------

y = np.sin(x) * np.exp(-x * 0.1)

# --------------------------------------
# Plot scientific curve
# --------------------------------------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    name="Damped Wave"
))

fig.update_layout(
    title="Scientific Plot: Damped Wave Simulation",
    xaxis_title="Time",
    yaxis_title="Amplitude"
)

fig.show()

"""
KEY IDEA:

✔ used in physics simulation
✔ exponential decay + wave
"""