# ======================================
# COUNTRY-LEVEL ANALYSIS MAP
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

# --------------------------------------
# Mobile users analysis
# --------------------------------------

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="mobile_users",
    title="Mobile Users by Country"
)

fig.show()

"""
KEY IDEA:

This helps analyze:
✔ technology adoption
✔ mobile penetration
✔ regional development

Example:
India & Bangladesh → high mobile usage
"""