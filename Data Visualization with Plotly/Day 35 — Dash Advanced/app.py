# ======================================
# DAY 35: MAIN DASH APP (MULTI-PAGE)
# ======================================

import dash
from dash import html, dcc

# Dash multi-page support
app = dash.Dash(__name__, use_pages=True)

# --------------------------------------
# MAIN LAYOUT (NAVIGATION MENU)
# --------------------------------------

app.layout = html.Div([

    html.H1("📊 Advanced Business Dashboard"),

    # Navigation links between pages
    html.Div([
        dcc.Link("Home", href="/"),
        " | ",
        dcc.Link("Sales Page", href="/sales"),
        " | ",
        dcc.Link("Profit Page", href="/profit")
    ]),

    html.Hr(),

    # This renders selected page
    dash.page_container
])

# --------------------------------------
# RUN SERVER
# --------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)

"""
KEY IDEA:

✔ use_pages=True → multi-page app
✔ page_container → loads pages dynamically
✔ dcc.Link → navigation system
"""