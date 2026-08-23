# ======================================
# DAY 40: PLOT SELECTION STRATEGY
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("master_data.csv")

# --------------------------------------
# 1. LINE CHART → Time series (trend)
# --------------------------------------

fig1 = px.line(df, x="date", y="sales", title="📈 Sales Trend (Line Chart)")
fig1.show()

# --------------------------------------
# 2. BAR CHART → Category comparison
# --------------------------------------

fig2 = px.bar(df, x="product", y="profit", title="📊 Profit by Product")
fig2.show()

# --------------------------------------
# 3. SCATTER → Relationship analysis
# --------------------------------------

fig3 = px.scatter(df, x="ad_spend", y="sales", title="📍 Ad Spend vs Sales")
fig3.show()

"""
KEY IDEA:

✔ Line → trends
✔ Bar → comparison
✔ Scatter → relationship
"""