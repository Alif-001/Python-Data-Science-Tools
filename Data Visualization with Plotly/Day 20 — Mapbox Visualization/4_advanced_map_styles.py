# ======================================
# ADVANCED MAPBOX STYLES
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

# --------------------------------------
# Advanced styling + scaling
# --------------------------------------

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="users",
    color="users",
    hover_name="place",
    color_continuous_scale="Viridis",
    zoom=2,
    title="Advanced Mapbox Visualization"
)

# Map style options:
# "open-street-map"
# "carto-positron"
# "carto-darkmatter"

fig.update_layout(
    mapbox_style="carto-darkmatter"
)

fig.show()

"""
KEY IDEA:

This is production-level map:
✔ multiple layers of data
✔ color + size encoding
✔ modern dark theme

Used in dashboards & analytics tools
"""