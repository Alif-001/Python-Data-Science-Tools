# 06_bandwidth_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BANDWIDTH (bw_adjust)

# --------------------------------------------

# Controls smoothness of curve

# --------------------------------------------

# Small bandwidth → sharp curve (less smooth)

sns.kdeplot(
data=tips,
x="total_bill",
bw_adjust=0.3
)

plt.title("Low Bandwidth (Sharp Curve)")
plt.show()

# Large bandwidth → very smooth curve

sns.kdeplot(
data=tips,
x="total_bill",
bw_adjust=2
)

plt.title("High Bandwidth (Smooth Curve)")
plt.show()

# --------------------------------------------

# IDEA:

# - low bw → detailed but noisy

# - high bw → smooth but less detail

# --------------------------------------------
