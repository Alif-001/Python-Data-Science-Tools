# ======================================
# INTERNET USERS VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

# --------------------------------------
# Internet usage map
# --------------------------------------

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="internet_users",
    title="Internet Users by Country"
)

fig.show()

"""
KEY IDEA:

This shows:
✔ digital adoption
✔ internet penetration
✔ connectivity gaps

Useful for:
✔ telecom analysis
✔ digital economy studies
"""