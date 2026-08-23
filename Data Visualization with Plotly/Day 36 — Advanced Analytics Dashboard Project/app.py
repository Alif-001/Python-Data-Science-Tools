# ======================================
# DAY 36: ADVANCED ANALYTICS DASHBOARD
# ======================================

import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("data.csv")

# --------------------------------------
# Initialize Dash app
# --------------------------------------

app = dash.Dash(__name__)

# --------------------------------------
# APP LAYOUT (UI DESIGN)
# --------------------------------------

app.layout = html.Div([

    html.H1("📊 Business Analytics Dashboard"),

    # -------------------------------
    # FILTER SECTION
    # -------------------------------

    html.Div([

        # Region filter
        dcc.Dropdown(
            id="region-filter",
            options=[{"label": r, "value": r} for r in df["region"].unique()],
            value="Dhaka",
            clearable=False
        ),

        # Category filter
        dcc.Dropdown(
            id="category-filter",
            options=[{"label": c, "value": c} for c in df["category"].unique()],
            value="Electronics",
            clearable=False
        )
    ]),

    html.Br(),

    # -------------------------------
    # KPI CARDS SECTION
    # -------------------------------

    html.Div(id="kpi-section"),

    html.Br(),

    # -------------------------------
    # GRAPHS SECTION
    # -------------------------------

    dcc.Graph(id="sales-chart"),
    dcc.Graph(id="profit-chart")
])

# --------------------------------------
# CALLBACK (INTERACTIVE FILTER LOGIC)
# --------------------------------------

@app.callback(
    [
        Output("kpi-section", "children"),
        Output("sales-chart", "figure"),
        Output("profit-chart", "figure")
    ],
    [
        Input("region-filter", "value"),
        Input("category-filter", "value")
    ]
)

def update_dashboard(region, category):

    # ----------------------------------
    # FILTER DATA
    # ----------------------------------

    filtered_df = df[
        (df["region"] == region) &
        (df["category"] == category)
    ]

    # ----------------------------------
    # KPI CALCULATIONS
    # ----------------------------------

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()
    customers = filtered_df["customer"].nunique()

    # KPI UI (simple cards)
    kpis = html.Div([

        html.H3(f"Total Sales: {total_sales}"),
        html.H3(f"Total Profit: {total_profit}"),
        html.H3(f"Customers: {customers}")

    ])

    # ----------------------------------
    # SALES CHART
    # ----------------------------------

    sales_fig = px.bar(
        filtered_df,
        x="customer",
        y="sales",
        title="Customer Sales"
    )

    # ----------------------------------
    # PROFIT CHART
    # ----------------------------------

    profit_fig = px.bar(
        filtered_df,
        x="customer",
        y="profit",
        title="Customer Profit"
    )

    return kpis, sales_fig, profit_fig

# --------------------------------------
# RUN SERVER
# --------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)

"""
KEY IDEA:

✔ filtering system (core analytics feature)
✔ KPI computation
✔ dynamic dashboard updates

This is REAL business dashboard logic
"""