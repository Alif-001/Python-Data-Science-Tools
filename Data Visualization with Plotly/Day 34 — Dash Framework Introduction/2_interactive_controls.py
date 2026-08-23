# ======================================
# DASH WITH INTERACTIVE CONTROLS
# ======================================

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_data.csv")

app = dash.Dash(__name__)

# --------------------------------------
# APP LAYOUT (UI DESIGN)
# --------------------------------------

app.layout = html.Div([

    html.H2("Interactive Sales Dashboard"),

    # Dropdown control (user input)
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Sales", "value": "sales"},
            {"label": "Profit", "value": "profit"}
        ],
        value="sales"
    ),

    # Graph output
    dcc.Graph(id="graph")
])

# --------------------------------------
# CALLBACK (core of Dash)
# --------------------------------------

@app.callback(
    Output("graph", "figure"),
    Input("metric-dropdown", "value")
)

def update_graph(selected_metric):

    fig = px.line(
        df,
        x="month",
        y=selected_metric,
        title=f"{selected_metric.capitalize()} Over Time"
    )

    return fig

# --------------------------------------
# Run app
# --------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)

"""
KEY IDEA:

Callback = brain of Dash app

✔ input → dropdown
✔ output → graph
✔ dynamic updates in real-time
"""