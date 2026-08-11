import matplotlib.pyplot as plt

"""
MULTIPLE HISTOGRAMS
-------------------
Compare two datasets in same graph.
"""

class_a = [45, 50, 55, 60, 65, 70, 75]
class_b = [50, 55, 60, 65, 70, 75, 80]

plt.hist(class_a, bins=5, alpha=0.6, label="Class A", color="blue")
plt.hist(class_b, bins=5, alpha=0.6, label="Class B", color="red")

plt.title("Class A vs Class B Distribution")
plt.legend()

plt.show()