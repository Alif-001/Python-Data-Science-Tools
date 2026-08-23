# ======================================
# COLOR + SIZE MAPPING IN GEO MAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

# --------------------------------------
# Advanced geo visualization
# --------------------------------------

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    color="gdp",
    hover_name="city",
    color_continuous_scale="Viridis",
    title="Advanced Geo Visualization"
)

# Improve map style
fig.update_geos(
    showcountries=True,
    showcoastlines=True
)

fig.show()

"""
KEY IDEA:

Now we combine:
✔ location (lat/lon)
✔ size (population)
✔ color (GDP)

This is used in real dashboards
"""