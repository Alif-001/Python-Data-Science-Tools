# ======================================
# DENSITY HISTOGRAM
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

# --------------------------------------
# Density histogram
# --------------------------------------

fig = px.histogram(
    df,
    x="math_score",
    histnorm="probability density",
    nbins=6,
    title="Density Histogram of Math Scores"
)

fig.show()

"""
KEY IDEA:

histnorm="probability density"

→ converts frequency into density

Useful in:
✔ statistics
✔ probability analysis
✔ machine learning
"""