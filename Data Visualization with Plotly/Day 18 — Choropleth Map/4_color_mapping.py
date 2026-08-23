# ======================================
# COLOR MAPPING IN CHOROPLETH
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

# --------------------------------------
# Advanced color styling
# --------------------------------------

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="gdp",
    color_continuous_scale="Viridis",
    title="GDP Color Mapping (Advanced)"
)

# Improve layout
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True)
)

fig.show()

"""
KEY IDEA:

color_continuous_scale controls:
✔ visual style
✔ clarity of comparison

Viridis is best for readability
"""