# 07_real_world_segmentation.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------

# SIMULATED CUSTOMER DATA

# --------------------------------------------

data = pd.DataFrame({
"Spending": [200, 300, 150, 400, 500, 250],
"Visits": [5, 7, 3, 10, 12, 6],
"Engagement": [30, 40, 20, 60, 80, 35]
})

# scale

data_scaled = (data - data.mean()) / data.std()

# --------------------------------------------

# CLUSTERMAP FOR SEGMENTATION

# --------------------------------------------

sns.clustermap(
data_scaled,
cmap="YlGnBu"
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - groups similar customers

# --------------------------------------------
