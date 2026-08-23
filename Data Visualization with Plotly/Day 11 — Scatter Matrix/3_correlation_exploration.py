# ======================================
# CORRELATION EXPLORATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Scatter matrix with trend insight
# --------------------------------------

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks"],
    color="marks",
    title="Correlation Exploration using Scatter Matrix"
)

# Improve visibility
fig.update_traces(diagonal_visible=False)

fig.show()

"""
KEY IDEA:

We can visually detect:

✔ positive correlation
✔ negative correlation
✔ no correlation

Example:
- study_hours ↑ → marks ↑
- sleep_hours → moderate effect
"""