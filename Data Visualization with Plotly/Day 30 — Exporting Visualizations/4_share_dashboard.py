# ======================================
# SHAREABLE DASHBOARD (PRODUCTION STYLE)
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("export_data.csv")

# Create interactive dashboard
fig = px.line(
    df,
    x="month",
    y=["sales", "profit"],
    title="Shareable Business Dashboard"
)

# --------------------------------------
# SAVE MULTIPLE FORMATS
# --------------------------------------

# 1. Interactive HTML
fig.write_html("dashboard.html")

# 2. Image
fig.write_image("dashboard.png")

# 3. PDF report
fig.write_image("dashboard.pdf")

fig.show()

"""
KEY IDEA:

This is REAL production workflow:

✔ HTML → interactive web dashboard
✔ PNG → presentation slides
✔ PDF → business report

One chart → multiple outputs
"""