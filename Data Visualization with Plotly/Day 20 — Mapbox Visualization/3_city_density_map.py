# ======================================
# CITY ACTIVITY MAP (DENSITY STYLE)
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

# --------------------------------------
# Color represents activity level
# --------------------------------------

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="activity",
    size="users",
    hover_name="place",
    zoom=2,
    title="City Activity Map"
)

fig.update_layout(
    mapbox_style="carto-positron"
)

fig.show()

"""
KEY IDEA:

Now we combine:
✔ location
✔ user activity
✔ intensity levels

Useful for:
✔ traffic analysis
✔ user behavior tracking
"""