# ======================================
# HOME PAGE
# ======================================

import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([

    html.H2("🏠 Home Dashboard"),

    html.P("Welcome to advanced Dash multi-page system."),

    html.Ul([
        html.Li("Sales Analytics Page"),
        html.Li("Profit Analytics Page"),
        html.Li("Dynamic Dashboards")
    ])
])

"""
KEY IDEA:

✔ register_page() = creates page
✔ path="/" = homepage
"""