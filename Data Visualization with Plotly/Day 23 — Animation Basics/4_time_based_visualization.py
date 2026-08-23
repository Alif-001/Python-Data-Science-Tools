# ======================================
# TIME-BASED ANIMATION VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("yearly_sales.csv")

# --------------------------------------
# Advanced animated chart
# --------------------------------------

fig = px.scatter(
    df,
    x="sales",
    y="profit",

    size="sales",
    color="country",

    animation_frame="year",

    # keeps bubble size consistent
    size_max=60,

    hover_name="country",

    title="Time-Based Business Visualization"
)

# Improve animation speed/layout
fig.update_layout(
    xaxis_title="Sales",
    yaxis_title="Profit"
)

fig.show()

"""
KEY IDEA:

This combines:
✔ animation
✔ color encoding
✔ bubble scaling
✔ time-based analysis

Used in professional dashboards
"""