# ======================================
# SCIENTIFIC SURFACE VISUALIZATION
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Simulate scientific data
# --------------------------------------

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

# Gaussian-like scientific surface
Z = np.exp(-(X**2 + Y**2) / 30)

# --------------------------------------
# Create scientific surface plot
# --------------------------------------

fig = go.Figure(
    data=[go.Surface(z=Z, x=X, y=Y)]
)

fig.update_layout(
    title="Scientific Surface Visualization"
)

fig.show()

"""
KEY IDEA:

Scientific surfaces are used for:
✔ simulations
✔ heat distributions
✔ physics calculations
✔ probability surfaces

Center peak = highest intensity
"""