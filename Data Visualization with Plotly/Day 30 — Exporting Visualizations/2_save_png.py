# ======================================
# SAVE AS PNG IMAGE
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("export_data.csv")

fig = px.bar(df, x="month", y="sales", title="Sales Report")

# --------------------------------------
# SAVE AS PNG
# --------------------------------------

fig.write_image("sales_chart.png")

fig.show()

"""
IMPORTANT NOTE:

To save PNG you need:
pip install kaleido

KEY IDEA:
✔ static image export
✔ good for reports
✔ PowerPoint / documents
"""