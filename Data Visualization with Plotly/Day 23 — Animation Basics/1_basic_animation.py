# ======================================
# DAY 23: BASIC ANIMATION
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("yearly_sales.csv")

# --------------------------------------
# Basic animated scatter plot
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    # animation_frame creates motion over time
    animation_frame="year",

    # point label
    hover_name="country",

    title="Basic Animated Visualization"
)

fig.show()

"""
KEY IDEA:

animation_frame=
✔ creates animation over time
✔ each frame = one year

The chart changes automatically:
2020 → 2021 → 2022 → 2023
"""