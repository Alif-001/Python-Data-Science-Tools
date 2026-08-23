# ======================================
# ANIMATED SCATTER PLOT
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("yearly_sales.csv")

# --------------------------------------
# Bubble animation
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    # bubble size
    size="sales",

    # bubble color
    color="country",

    # time animation
    animation_frame="year",

    hover_name="country",

    title="Animated Bubble Scatter Plot"
)

fig.show()

"""
KEY IDEA:

Now animation includes:
✔ moving points
✔ changing bubble sizes
✔ dynamic comparison

This creates powerful storytelling
"""