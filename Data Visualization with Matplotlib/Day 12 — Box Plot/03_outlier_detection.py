import matplotlib.pyplot as plt

"""
OUTLIER DETECTION
-----------------
Outliers = unusual values far from normal range
"""

data = [10, 12, 13, 15, 14, 13, 12, 11, 100]  # 100 is outlier

plt.boxplot(data)

plt.title("Outlier Detection Example")

plt.show()