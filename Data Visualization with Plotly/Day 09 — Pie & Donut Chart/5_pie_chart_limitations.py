# ======================================
# PIE CHART LIMITATIONS
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Create dataset with too many categories
# --------------------------------------

data = {
    "category": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],
    "value": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# --------------------------------------
# Pie chart with many categories
# --------------------------------------

fig = px.pie(
    df,
    names="category",
    values="value",
    title="Pie Chart Limitation Example"
)

fig.show()

"""
IMPORTANT LESSON:

Pie charts become hard to read when:
❌ too many categories
❌ values are very similar

In these cases:
✔ bar chart is usually better

RULE:
Use pie chart only for:
✔ small number of categories
✔ clear percentage comparison
"""