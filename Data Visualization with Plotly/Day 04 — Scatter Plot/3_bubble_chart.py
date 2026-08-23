# ======================================
# BUBBLE CHART (IMPORTANT)
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

# --------------------------------------
# Bubble chart using "size"
# --------------------------------------

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    size="attendance",  # bubble size
    color="gender",
    title="Bubble Chart: Study vs Marks vs Attendance"
)

fig.show()

"""
KEY IDEA:

size=
→ adds third dimension

So now we have:
✔ X = study_hours
✔ Y = marks
✔ SIZE = attendance
✔ COLOR = gender
"""