# ======================================
# DAY 20: BASIC MAPBOX VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("location_data.csv")

# --------------------------------------
# Basic Mapbox scatter plot
# --------------------------------------

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="place",
    zoom=2,
    title="Basic Mapbox Visualization"
)

# IMPORTANT: Mapbox requires style
fig.update_layout(
    mapbox_style="open-street-map"
)

fig.show()

"""
KEY IDEA:

Mapbox gives:
✔ smooth zooming map
✔ real-world interaction
✔ modern map UI

Each point = a location
"""