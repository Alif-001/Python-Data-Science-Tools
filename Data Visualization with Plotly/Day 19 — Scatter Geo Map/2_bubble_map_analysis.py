# ======================================
# BUBBLE MAP ANALYSIS
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

# --------------------------------------
# Bubble size = population
# --------------------------------------

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",   # bubble size
    hover_name="city",
    title="Population Bubble Map"
)

fig.show()

"""
KEY IDEA:

Bubble maps show:
✔ city importance
✔ population comparison
✔ visual weight of regions

Bigger bubble = more population
"""