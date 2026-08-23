# ======================================
# STATISTICAL VIEW USING CONTOUR
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Combine contour + scatter effect
# --------------------------------------

fig = px.density_contour(
    df,
    x="attendance",
    y="marks",
    title="Attendance vs Marks - Statistical View"
)

# Add scatter points on top (important)
fig.update_traces(contours_coloring="fill")

fig.show()

"""
KEY IDEA:

Contour plot helps answer:

✔ where most students fall
✔ relationship between variables
✔ distribution structure

Filled contours = heat-like statistical zones
"""