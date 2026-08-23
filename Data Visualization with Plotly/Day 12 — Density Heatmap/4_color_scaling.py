# ======================================
# COLOR SCALING IN HEATMAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Heatmap with color scale customization
# --------------------------------------

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    title="Heatmap with Color Scaling",
    color_continuous_scale="Viridis"
)

fig.show()

"""
KEY IDEA:

color_continuous_scale controls:
✔ how intensity is shown
✔ visual clarity

Popular scales:
- Viridis (best default)
- Hot
- Blues
- Plasma
"""