# 06_real_dataset_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------

# SMALL CUSTOM DATASET (NO CSV NEEDED)

# --------------------------------------------

data = {
"Math": [80, 90, 70, 60, 85],
"Physics": [78, 88, 72, 65, 80],
"Chemistry": [82, 91, 68, 70, 86]
}

df = pd.DataFrame(data)

corr = df.corr()

# --------------------------------------------

# HEATMAP FOR STUDENT SCORES

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="YlGnBu"
)

plt.title("Subject Score Correlation")
plt.show()

# --------------------------------------------

# INSIGHT:

# - see which subjects are related

# --------------------------------------------
