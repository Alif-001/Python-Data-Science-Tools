# ======================================
# DENSITY REGIONS VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Add coloring to contour regions
# --------------------------------------

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    color="marks",   # adds intensity variation
    title="Density Regions (Colored Contours)"
)

fig.show()

"""
KEY IDEA:

Contour lines create:
✔ zones of similar density
✔ group separation
✔ smooth pattern visualization

Color helps show intensity differences
"""