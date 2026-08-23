# ======================================
# GPS STYLE TRACKING MAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

# --------------------------------------
# GPS-style visualization using size
# --------------------------------------

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="users",   # bigger = more users
    hover_name="place",
    zoom=2,
    title="GPS User Activity Map"
)

fig.update_layout(
    mapbox_style="open-street-map"
)

fig.show()

"""
KEY IDEA:

We simulate GPS tracking:
✔ more users → bigger bubble
✔ location-based activity tracking

Used in delivery apps, ride apps
"""