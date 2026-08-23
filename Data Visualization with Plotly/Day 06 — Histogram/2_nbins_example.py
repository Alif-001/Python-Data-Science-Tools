# ======================================
# USING NBINS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

# --------------------------------------
# Control number of bins
# --------------------------------------

fig = px.histogram(
    df,
    x="math_score",
    nbins=5,   # number of bars/ranges
    title="Histogram with 5 Bins"
)

fig.show()

"""
KEY IDEA:

nbins=
→ controls histogram grouping

Smaller nbins:
✔ broader ranges

Larger nbins:
✔ more detailed distribution
"""