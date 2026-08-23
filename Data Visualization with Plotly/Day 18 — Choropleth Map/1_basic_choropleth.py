# ======================================
# DAY 18: BASIC CHOROPLETH MAP
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("country_data.csv")

# --------------------------------------
# Basic choropleth map
# --------------------------------------

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="gdp",
    title="World GDP Visualization"
)

fig.show()

"""
KEY IDEA:

Choropleth map shows:
✔ geographic comparison
✔ value-based coloring
✔ country-level analysis

Darker color = higher value
"""