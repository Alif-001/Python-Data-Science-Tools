# 05_residual_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_data.csv")

X = df[["study_hours"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

df["predicted"] = model.predict(X)

# --------------------------------------------

# RESIDUAL = ACTUAL - PREDICTED

# --------------------------------------------

df["residual"] = df["final_score"] - df["predicted"]

# --------------------------------------------

# RESIDUAL PLOT

# --------------------------------------------

sns.scatterplot(
data=df,
x="predicted",
y="residual"
)

plt.axhline(0, color="red")
plt.title("Residual Analysis")
plt.show()

# --------------------------------------------

# IDEA:

# - shows model error pattern

# --------------------------------------------
