# ======================================
# LAYOUT BASICS + THEMES
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales.csv")

# --------------------------------------
# Theme / Template system
# --------------------------------------
"""
Plotly has built-in themes:
- plotly
- plotly_dark
- ggplot2
- seaborn
- simple_white
"""

fig = px.bar(
    df,
    x="day",
    y="sales",
    color="region",
    title="Sales by Day (Styled)"
)

# --------------------------------------
# Layout customization
# --------------------------------------
fig.update_layout(
    template="plotly_dark",  # theme
    title="Styled Sales Chart",
    xaxis_title="Day of Week",
    yaxis_title="Sales",
    font=dict(size=14)
)

fig.show()

"""
LAYOUT = overall design of chart
"""