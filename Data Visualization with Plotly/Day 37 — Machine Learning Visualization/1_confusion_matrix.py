# ======================================
# DAY 37: CONFUSION MATRIX VISUALIZATION
# ======================================

import pandas as pd
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load data
df = pd.read_csv("student_data.csv")

# Features and target
X = df[["hours_studied", "attendance"]]
y = df["passed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# --------------------------------------
# Plot confusion matrix
# --------------------------------------

fig = ff.create_annotated_heatmap(
    z=cm,
    x=["Pred 0", "Pred 1"],
    y=["Actual 0", "Actual 1"],
    colorscale="Blues"
)

fig.update_layout(title="Confusion Matrix")

fig.show()

"""
KEY IDEA:

✔ shows correct vs wrong predictions
✔ evaluates classification models
"""