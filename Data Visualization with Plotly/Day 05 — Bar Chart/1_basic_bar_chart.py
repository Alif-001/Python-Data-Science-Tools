# ======================================
# DAY 5: BASIC BAR CHART
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create basic bar chart
# --------------------------------------

fig = px.bar(
    df,
    x="month",
    y="sales",
    title="Monthly Sales"
)

# Show chart
fig.show()

"""
KEY IDEA:

Bar chart is used for:
✔ category comparison
✔ comparing values
✔ showing rankings

Examples:
- sales by month
- students by class
- products by revenue
"""