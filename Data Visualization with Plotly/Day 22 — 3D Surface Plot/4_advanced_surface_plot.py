# ======================================
# ADVANCED 3D SURFACE PLOT
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Generate advanced mathematical surface
# --------------------------------------

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

# --------------------------------------
# Advanced surface visualization
# --------------------------------------

fig = go.Figure(
    data=[
        go.Surface(
            z=Z,
            x=X,
            y=Y,
            colorscale="Viridis"
        )
    ]
)

# Improve scene layout
fig.update_layout(
    title="Advanced Surface Plot",
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Height (Z)"
    )
)

fig.show()

"""
KEY IDEA:

Advanced surface plots support:
✔ custom color scales
✔ scientific rendering
✔ interactive rotation
✔ terrain-style visualization
"""