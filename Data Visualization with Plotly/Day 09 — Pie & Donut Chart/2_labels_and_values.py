# ======================================
# LABELS & VALUES
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

# --------------------------------------
# Customize labels and values
# --------------------------------------

fig = px.pie(
    df,
    names="brand",
    values="sales",
    title="Brand-wise Sales Share"
)

# --------------------------------------
# Show labels + percentage
# --------------------------------------

fig.update_traces(
    textinfo="label+percent"
)

fig.show()

"""
KEY IDEA:

names=
→ category names

values=
→ numerical contribution

textinfo=
→ controls displayed text
"""