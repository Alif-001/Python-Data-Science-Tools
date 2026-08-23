# ======================================
# PROFIT ANALYTICS PAGE
# ======================================

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv("data.csv")

fig = px.bar(df, x="month", y="profit", title="Profit Analysis")

layout = html.Div([

    html.H2("💰 Profit Analytics"),

    dcc.Graph(figure=fig)
])

"""
KEY IDEA:

✔ separate business metrics
✔ clean modular design
"""