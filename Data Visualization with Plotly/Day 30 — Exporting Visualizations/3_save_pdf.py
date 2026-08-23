# ======================================
# SAVE AS PDF REPORT
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("export_data.csv")

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    title="Sales vs Profit Report"
)

# --------------------------------------
# SAVE AS PDF
# --------------------------------------

fig.write_image("sales_report.pdf")

fig.show()

"""
KEY IDEA:

PDF export:
✔ professional reporting format
✔ used in business reports
✔ printable dashboards
"""