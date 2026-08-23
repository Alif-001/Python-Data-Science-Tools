# ======================================
# SALES ANALYTICS PAGE
# ======================================

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv("data.csv")

fig = px.line(df, x="month", y="sales", title="Sales Trend")

layout = html.Div([

    html.H2("📈 Sales Analytics"),

    dcc.Graph(figure=fig)
])

"""
KEY IDEA:

✔ each page has its own chart
✔ modular dashboard design
"""