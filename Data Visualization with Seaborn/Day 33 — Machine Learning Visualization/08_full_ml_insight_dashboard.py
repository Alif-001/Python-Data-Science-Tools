# 08_full_ml_insight_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_data.csv")

# MODEL

X = df[["study_hours"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

df["predicted"] = model.predict(X)
df["residual"] = df["final_score"] - df["predicted"]

# --------------------------------------------

# DASHBOARD

# --------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# FEATURE RELATIONSHIP

sns.scatterplot(data=df, x="study_hours", y="final_score", ax=axes[0,0])
axes[0,0].set_title("Study vs Score")

# PREDICTION

sns.lineplot(data=df, x="study_hours", y="predicted", ax=axes[0,1])
axes[0,1].set_title("Model Prediction")

# RESIDUAL

sns.scatterplot(data=df, x="predicted", y="residual", ax=axes[1,0])
axes[1,0].axhline(0, color="red")
axes[1,0].set_title("Residuals")

# DISTRIBUTION

sns.histplot(df["final_score"], kde=True, ax=axes[1,1])
axes[1,1].set_title("Target Distribution")

plt.tight_layout()
plt.show()

# --------------------------------------------

# FINAL INSIGHT:

# - full ML understanding in one view

# --------------------------------------------
