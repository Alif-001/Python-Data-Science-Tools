# ======================================
# DAY 6: BASIC HISTOGRAM
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("student_scores.csv")

print(df)

# --------------------------------------
# Create histogram
# --------------------------------------

fig = px.histogram(
    df,
    x="math_score",
    title="Distribution of Math Scores"
)

fig.show()

"""
KEY IDEA:

Histogram shows:
✔ data distribution
✔ frequency of values
✔ spread of data

Unlike bar charts:
- Histogram groups continuous numbers into ranges
"""