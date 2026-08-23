# 06_large_synthetic_clustermap.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------------------------

# SYNTHETIC LARGE DATASET

# --------------------------------------------

np.random.seed(42)

df = pd.DataFrame({
"Feature_A": np.random.rand(50),
"Feature_B": np.random.rand(50) * 2,
"Feature_C": np.random.rand(50) * 3,
"Feature_D": np.random.rand(50) * 4,
"Feature_E": np.random.rand(50) * 5,
})

# scale data

df_scaled = (df - df.mean()) / df.std()

# --------------------------------------------

# CLUSTERMAP

# --------------------------------------------

sns.clustermap(df_scaled, cmap="coolwarm")

plt.show()

# --------------------------------------------

# IDEA:

# - real-world datasets behave like this

# --------------------------------------------
