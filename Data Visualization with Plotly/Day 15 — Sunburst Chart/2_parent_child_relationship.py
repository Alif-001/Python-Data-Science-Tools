# ======================================
# PARENT-CHILD RELATIONSHIP VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

# --------------------------------------
# Full hierarchy visualization
# --------------------------------------

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    title="Full Parent → Child Relationship"
)

fig.show()

"""
KEY IDEA:

Hierarchy flow:

Company → Department → Team

This helps understand:
✔ organizational structure
✔ revenue contribution at each level
✔ dependency flow
"""