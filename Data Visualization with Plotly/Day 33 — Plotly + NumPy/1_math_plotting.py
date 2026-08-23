# ======================================
# DAY 33: MATHEMATICAL PLOTTING
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Create x values (0 → 10)
# --------------------------------------

x = np.linspace(0, 10, 100)

# --------------------------------------
# Mathematical functions
# --------------------------------------

y_sin = np.sin(x)
y_cos = np.cos(x)

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# Sine wave
fig.add_trace(go.Scatter(
    x=x,
    y=y_sin,
    mode="lines",
    name="sin(x)"
))

# Cosine wave
fig.add_trace(go.Scatter(
    x=x,
    y=y_cos,
    mode="lines",
    name="cos(x)"
))

fig.update_layout(
    title="Mathematical Functions (Sin & Cos)",
    xaxis_title="X",
    yaxis_title="Y"
)

fig.show()

"""
KEY IDEA:

✔ NumPy generates math data
✔ Plotly visualizes functions
✔ used in physics + engineering
"""