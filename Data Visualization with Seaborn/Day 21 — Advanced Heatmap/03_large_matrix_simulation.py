# 03_large_matrix_simulation.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------------------------

# CREATE LARGE SYNTHETIC DATASET

# --------------------------------------------

np.random.seed(42)

df = pd.DataFrame({
"A": np.random.rand(100),
"B": np.random.rand(100) * 2,
"C": np.random.rand(100) * 3,
"D": np.random.rand(100) * 4,
"E": np.random.rand(100) * 5,
"F": np.random.rand(100) * 6,
})

corr = df.corr()

# --------------------------------------------

# LARGE HEATMAP

# --------------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
corr,
annot=True,
cmap="viridis"
)

plt.title("Large Feature Correlation Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - real ML datasets behave like this

# --------------------------------------------
