# ======================================
# DAY 30: SAVE AS HTML (INTERACTIVE)
# ======================================

import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("export_data.csv")

# Create chart
fig = px.line(df, x="month", y="sales", title="Sales Dashboard")

# --------------------------------------
# SAVE AS HTML
# --------------------------------------

fig.write_html("sales_dashboard.html")

# Show in browser
fig.show()

"""
KEY IDEA:

HTML export:
✔ fully interactive
✔ zoom, hover, pan works
✔ can open in browser
✔ best for sharing dashboards
"""