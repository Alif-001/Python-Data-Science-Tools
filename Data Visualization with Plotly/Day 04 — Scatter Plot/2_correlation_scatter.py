# ======================================
# CORRELATION VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

# --------------------------------------
# Add color for better understanding
# --------------------------------------

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="passed",   # shows pass/fail grouping
    title="Study Hours vs Marks (Colored by Pass/Fail)"
)

fig.show()

"""
KEY IDEA:

color=
→ separates categories visually

Now we can clearly see:
✔ who passed
✔ who failed
✔ pattern differences
"""