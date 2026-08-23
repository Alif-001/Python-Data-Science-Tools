# ======================================
# PREDICTION VISUALIZATION
# ======================================

import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("student_data.csv")

X = df[["hours_studied"]]
y = df["passed"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predictions
df["prediction"] = model.predict(X)

# --------------------------------------
# Visualization
# --------------------------------------

fig = go.Figure()

# Actual values
fig.add_trace(go.Scatter(
    x=df["hours_studied"],
    y=df["passed"],
    mode="markers",
    name="Actual"
))

# Predicted values
fig.add_trace(go.Scatter(
    x=df["hours_studied"],
    y=df["prediction"],
    mode="lines+markers",
    name="Predicted"
))

fig.update_layout(
    title="Prediction vs Actual",
    xaxis_title="Hours Studied",
    yaxis_title="Pass (0/1)"
)

fig.show()

"""
KEY IDEA:

✔ compare model vs reality
✔ see prediction behavior
"""