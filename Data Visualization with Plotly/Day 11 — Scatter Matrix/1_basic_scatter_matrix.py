# ======================================
# DAY 11: BASIC SCATTER MATRIX
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("student_data.csv")

# --------------------------------------
# Scatter Matrix (Pair Plot)
# --------------------------------------

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks", "iq"],
    title="Scatter Matrix - Basic View"
)

fig.show()

"""
KEY IDEA:

Scatter Matrix shows:
✔ relationship between every pair of variables
✔ patterns in multidimensional data

If you have:
- 5 columns → it shows 5x5 grid

Very useful in:
✔ data exploration
✔ ML preprocessing
"""