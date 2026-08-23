# ======================================
# DAY 34: FIRST DASH APP
# ======================================

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# --------------------------------------
# Load data
# --------------------------------------

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create Plotly figure
# --------------------------------------

fig = px.line(df, x="month", y="sales", title="Sales Dashboard")

# --------------------------------------
# Initialize Dash app
# --------------------------------------

app = dash.Dash(__name__)

# --------------------------------------
# Layout = UI of web app
# --------------------------------------

app.layout = html.Div([
    
    html.H1("My First Dash Dashboard"),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

# --------------------------------------
# Run server
# --------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)

"""
KEY IDEA:

Dash = Web app builder

✔ html.Div → page layout
✔ dcc.Graph → Plotly chart
✔ app.run_server → runs website
"""