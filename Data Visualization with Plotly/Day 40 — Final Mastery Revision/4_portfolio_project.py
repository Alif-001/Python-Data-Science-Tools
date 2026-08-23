# ======================================
# PORTFOLIO READY PROJECT
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("master_data.csv")

# --------------------------------------
# STEP 1: CLEAN INSIGHTS
# --------------------------------------

region_sales = df.groupby("region")["sales"].sum().reset_index()
product_profit = df.groupby("product")["profit"].sum().reset_index()

# --------------------------------------
# STEP 2: VISUALS
# --------------------------------------

fig1 = px.bar(
    region_sales,
    x="region",
    y="sales",
    title="🌍 Sales by Region"
)

fig2 = px.bar(
    product_profit,
    x="product",
    y="profit",
    title="💰 Profit by Product"
)

fig3 = px.line(
    df,
    x="date",
    y="sales",
    title="📈 Sales Over Time"
)

# --------------------------------------
# STEP 3: SHOW ALL
# --------------------------------------

fig1.show()
fig2.show()
fig3.show()

"""
KEY IDEA:

✔ portfolio project = multiple insights
✔ shows real analyst skill
✔ job-ready project
"""