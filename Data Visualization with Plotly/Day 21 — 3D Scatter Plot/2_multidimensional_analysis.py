# ======================================
# MULTI-DIMENSIONAL ANALYSIS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Add color + size dimensions
# --------------------------------------

fig = px.scatter_3d(
    df,
    x="study_hours",
    y="sleep_hours",
    z="marks",
    color="attendance",   # extra dimension
    size="attendance",    # extra dimension
    hover_name="student",
    title="Multi-Dimensional Student Analysis"
)

fig.show()

"""
KEY IDEA:

Now we visualize:
✔ 3D position
✔ color intensity
✔ point size

This creates multi-dimensional insight
"""