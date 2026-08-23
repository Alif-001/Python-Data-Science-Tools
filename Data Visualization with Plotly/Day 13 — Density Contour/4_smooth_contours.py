# ======================================
# SMOOTH CONTOUR VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Smooth contour visualization
# --------------------------------------

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    nbinsx=20,
    nbinsy=20,
    title="Smooth Density Contour"
)

fig.show()

"""
KEY IDEA:

nbins controls:
✔ smoothness of contour
✔ level of detail

More bins =
✔ smoother surface
✔ better precision

Less bins =
✔ rough but simple view
"""