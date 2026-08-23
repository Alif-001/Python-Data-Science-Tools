# ======================================
# FEATURE IMPORTANCE VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("student_data.csv")

X = df[["hours_studied", "attendance"]]
y = df["passed"]

model = LogisticRegression()
model.fit(X, y)

# Feature importance (coefficients)
importance = model.coef_[0]

features = X.columns

# Create DataFrame
feature_df = pd.DataFrame({
    "feature": features,
    "importance": importance
})

# --------------------------------------
# Plot feature importance
# --------------------------------------

fig = px.bar(
    feature_df,
    x="feature",
    y="importance",
    title="Feature Importance"
)

fig.show()

"""
KEY IDEA:

✔ shows which feature matters more
✔ helps model interpretability
"""