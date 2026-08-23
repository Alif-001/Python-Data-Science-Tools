# ======================================
# OUTLIER DETECTION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

# --------------------------------------
# Box plot for outlier detection
# --------------------------------------

fig = px.box(
    df,
    y="score",
    points="outliers",   # show only outliers
    title="Outlier Detection using Box Plot"
)

fig.show()

"""
KEY IDEA:

Outliers =
extremely unusual values

In our dataset:
- 100
- 95

are likely outliers.

Why important?
✔ anomaly detection
✔ fraud analysis
✔ data cleaning
✔ ML preprocessing
"""