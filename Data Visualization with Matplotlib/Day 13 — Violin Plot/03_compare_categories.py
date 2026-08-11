import matplotlib.pyplot as plt
import numpy as np

"""
COMPARING CATEGORIES
--------------------
Used to compare multiple groups.
"""

class_a = np.random.normal(60, 10, 100)
class_b = np.random.normal(70, 15, 100)
class_c = np.random.normal(80, 5, 100)

data = [class_a, class_b, class_c]

plt.violinplot(data)

plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])

plt.title("Category Comparison with Violin Plot")

plt.show()