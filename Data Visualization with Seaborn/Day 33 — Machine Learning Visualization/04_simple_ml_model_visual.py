# 04_simple_ml_model_visual.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# SIMPLE MODEL: study_hours → final_score

# --------------------------------------------

X = df[["study_hours"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

# predictions

df["predicted"] = model.predict(X)

# --------------------------------------------

# VISUALIZATION

# --------------------------------------------

sns.scatterplot(data=df, x="study_hours", y="final_score", label="Actual")
sns.lineplot(data=df, x="study_hours", y="predicted", label="Predicted")

plt.title("ML Prediction Visualization")
plt.show()

# --------------------------------------------

# IDEA:

# - compare real vs predicted

# --------------------------------------------
