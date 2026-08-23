# ======================================
# MATHEMATICAL SURFACE VISUALIZATION
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Create X and Y coordinate grid
# --------------------------------------

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

# --------------------------------------
# Mathematical function
# --------------------------------------

Z = np.sin(np.sqrt(X**2 + Y**2))

# --------------------------------------
# Surface visualization
# --------------------------------------

fig = go.Figure(
    data=[go.Surface(z=Z, x=X, y=Y)]
)

fig.update_layout(
    title="Mathematical Surface Plot"
)

fig.show()

"""
KEY IDEA:

We use:
✔ mathematical equations
✔ coordinate grids
✔ calculated height values

This creates wave-like surfaces
"""