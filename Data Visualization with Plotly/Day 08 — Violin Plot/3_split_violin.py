# ======================================
# SPLIT VIOLIN PLOT
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Compare gender distributions
# --------------------------------------

fig = px.violin(
    df,
    x="department",
    y="score",
    color="gender",
    box=True,
    points="all",
    title="Split Violin Plot by Gender"
)

# Split violins
fig.update_traces(
    side="positive",   # split effect
    meanline_visible=True
)

fig.show()

"""
KEY IDEA:

Split violin helps compare:
✔ male vs female
✔ different groups
✔ distribution differences

Very useful in statistics.
"""