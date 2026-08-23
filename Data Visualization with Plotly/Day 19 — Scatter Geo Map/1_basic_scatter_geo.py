# ======================================
# DAY 19: BASIC SCATTER GEO MAP
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("city_data.csv")

# --------------------------------------
# Basic geographic scatter plot
# --------------------------------------

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    hover_name="city",
    title="Cities on World Map"
)

fig.show()

"""
KEY IDEA:

Scatter Geo shows:
✔ exact location points
✔ interactive world map
✔ hover-based information

Each point = one city
"""