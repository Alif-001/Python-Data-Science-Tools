# 06_multivariate_eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# FULL MULTI VARIABLE VIEW

# --------------------------------------------

sns.pairplot(df)

plt.show()

# --------------------------------------------

# IDEA:

# - all relationships at once

# --------------------------------------------
