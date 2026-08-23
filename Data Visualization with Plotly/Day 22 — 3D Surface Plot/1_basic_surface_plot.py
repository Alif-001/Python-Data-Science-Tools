# ======================================
# DAY 22: BASIC 3D SURFACE PLOT
# ======================================

import numpy as np
import plotly.graph_objects as go

# --------------------------------------
# Create Z values (height matrix)
# --------------------------------------

z = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

# --------------------------------------
# Create surface plot
# --------------------------------------

fig = go.Figure(
    data=[go.Surface(z=z)]
)

# Add title
fig.update_layout(
    title="Basic 3D Surface Plot"
)

fig.show()

"""
KEY IDEA:

Surface plot shows:
✔ continuous 3D surface
✔ height/intensity variation
✔ mathematical landscape

z-values control height
"""