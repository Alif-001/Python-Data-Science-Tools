# ======================================
# CITY LEVEL GEO VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

# --------------------------------------
# Color by GDP
# --------------------------------------

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    color="gdp",
    hover_name="city",
    title="City GDP + Population Analysis"
)

fig.show()

"""
KEY IDEA:

This shows:
✔ economic strength by city
✔ population + GDP relationship
✔ global comparison

Color = GDP
Size = population
"""