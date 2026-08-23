# ======================================
# GROUP COMPARISON
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

# --------------------------------------
# Compare departments
# --------------------------------------

fig = px.box(
    df,
    x="department",
    y="score",
    color="department",
    points="all",
    title="Department-wise Score Comparison"
)

fig.show()

"""
KEY IDEA:

Using x=
creates multiple box plots.

Useful for:
✔ group comparison
✔ comparing distributions
✔ identifying best/worst groups

Now we can compare:
- CSE scores
- EEE scores
"""