# ======================================
# LIVE DASHBOARD (MULTI-COMPONENT)
# ======================================

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_data.csv")

app = dash.Dash(__name__)

# --------------------------------------
# UI Layout
# --------------------------------------

app.layout = html.Div([

    html.H1("Business Live Dashboard"),

    # Dropdown
    dcc.Dropdown(
        id="metric",
        options=[
            {"label": "Sales", "value": "sales"},
            {"label": "Profit", "value": "profit"}
        ],
        value="sales"
    ),

    # Slider (extra control)
    dcc.Slider(
        id="range-slider",
        min=0,
        max=len(df)-1,
        value=len(df),
        marks={i: df["month"][i] for i in range(len(df))},
        step=1
    ),

    # Graph
    dcc.Graph(id="live-graph")
])

# --------------------------------------
# Callback logic
# --------------------------------------

@app.callback(
    Output("live-graph", "figure"),
    Input("metric", "value"),
    Input("range-slider", "value")
)

def update_chart(metric, slider_value):

    # filter data dynamically
    filtered_df = df.iloc[:slider_value]

    fig = px.line(
        filtered_df,
        x="month",
        y=metric,
        title="Live Dashboard Simulation"
    )

    return fig

# --------------------------------------
# Run server
# --------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)

"""
KEY IDEA:

This app shows:

✔ dropdown control
✔ slider control
✔ dynamic filtering
✔ real dashboard behavior
"""