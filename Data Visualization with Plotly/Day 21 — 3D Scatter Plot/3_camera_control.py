# ======================================
# CAMERA CONTROL IN 3D PLOT
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Create 3D scatter plot
# --------------------------------------

fig = px.scatter_3d(
    df,
    x="study_hours",
    y="sleep_hours",
    z="marks",
    color="marks",
    title="3D Plot with Camera Control"
)

# --------------------------------------
# Adjust camera position
# --------------------------------------

fig.update_layout(
    scene_camera=dict(
        eye=dict(x=1.5, y=1.5, z=1.5)
    )
)

fig.show()

"""
KEY IDEA:

Camera control helps:
✔ rotate view
✔ inspect hidden points
✔ improve perspective

Interactive rotation is one of Plotly's strengths
"""