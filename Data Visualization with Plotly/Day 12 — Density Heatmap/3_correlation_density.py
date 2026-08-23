# ======================================
# CORRELATION DENSITY HEATMAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Add another density layer
# --------------------------------------

fig = px.density_heatmap(
    df,
    x="attendance",
    y="marks",
    title="Attendance vs Marks Density"
)

fig.show()

"""
KEY IDEA:

We can visually see correlation:

✔ attendance ↑ → marks ↑ (positive trend)
✔ clusters show strong patterns

This is better than scatter plot when data is large.
"""