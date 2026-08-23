# ======================================
# DAY 39: EXPERIMENT DATA VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

# Load experimental data
df = pd.read_csv("experiment_data.csv")

# --------------------------------------
# Temperature over time
# --------------------------------------

fig1 = px.line(
    df,
    x="time",
    y="temperature",
    title="Temperature vs Time"
)

fig1.show()

# --------------------------------------
# Pressure over time
# --------------------------------------

fig2 = px.line(
    df,
    x="time",
    y="pressure",
    title="Pressure vs Time"
)

fig2.show()

"""
KEY IDEA:

✔ experimental data analysis
✔ used in labs + research papers
"""