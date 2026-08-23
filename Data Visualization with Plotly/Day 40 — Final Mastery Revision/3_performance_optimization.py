# ======================================
# PERFORMANCE OPTIMIZATION IN PLOTLY
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("master_data.csv")

# --------------------------------------
# TIP 1: Use smaller datasets for speed
# --------------------------------------

df_small = df.head(5)

# --------------------------------------
# TIP 2: Reduce marker complexity
# --------------------------------------

fig = px.scatter(
    df_small,
    x="sales",
    y="profit",
    title="Optimized Scatter Plot"
)

# --------------------------------------
# TIP 3: Avoid heavy styling in loops
# --------------------------------------

fig.update_traces(marker=dict(size=8))

fig.show()

"""
KEY IDEA:

✔ smaller data = faster plots
✔ avoid unnecessary complexity
✔ optimize for dashboards
"""