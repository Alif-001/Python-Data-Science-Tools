# ======================================
# HEATMAP WITH BINS (CONTROLLED GROUPING)
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Control bin size (resolution)
# --------------------------------------

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    nbinsx=6,
    nbinsy=6,
    title="Heatmap with Controlled Bins"
)

fig.show()

"""
KEY IDEA:

nbinsx / nbinsy =
→ controls how data is grouped

Small bins:
✔ detailed view

Large bins:
✔ smoother heatmap
"""