# ======================================
# MULTIVARIABLE ANALYSIS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

# --------------------------------------
# Add color grouping (VERY IMPORTANT)
# --------------------------------------

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks"],
    color="iq",   # adds intelligence grouping
    title="Multivariable Analysis with Color Encoding"
)

fig.show()

"""
KEY IDEA:

color=
→ adds extra dimension

Now we can see:
✔ how IQ affects other variables
✔ pattern clusters
✔ data grouping behavior
"""