# ======================================
# MODEL EVALUATION DASHBOARD
# ======================================

import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv("student_data.csv")

X = df[["hours_studied", "attendance"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, pred)
prec = precision_score(y_test, pred)
rec = recall_score(y_test, pred)

# --------------------------------------
# Dashboard style visualization
# --------------------------------------

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number",
    value=acc,
    title={"text": "Accuracy"}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=prec,
    title={"text": "Precision"},
    domain={"x": [0.5, 1], "y": [0.5, 1]}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=rec,
    title={"text": "Recall"},
    domain={"x": [0, 0.5], "y": [0, 0.5]}
))

fig.update_layout(title="Model Evaluation Dashboard")

fig.show()

"""
KEY IDEA:

✔ evaluates ML model performance
✔ shows metrics visually
"""