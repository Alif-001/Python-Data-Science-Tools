# ==========================
# FIRST INTERACTIVE CHART
# ==========================

import pandas as pd
import plotly.express as px

# --------------------------
# Load dataset
# --------------------------
df = pd.read_csv("data.csv")

# Show data (just to understand)
print(df)

# --------------------------
# Create first interactive line chart
# --------------------------

fig = px.line(
    df,
    x="day",
    y="sales",
    title="Daily Sales Trend"
)

# --------------------------
# Show chart
# --------------------------
fig.show()

"""
IMPORTANT CONCEPT:

fig.show()

- This opens an interactive chart in browser
- You can zoom, hover, pan
- This is the key difference vs Matplotlib
"""