import matplotlib.pyplot as plt

"""
MULTIPLE BOX PLOTS
------------------
Used to compare different groups.
"""

class_a = [60, 65, 70, 75, 80]
class_b = [55, 60, 65, 70, 75]
class_c = [70, 75, 80, 85, 90]

data = [class_a, class_b, class_c]

plt.boxplot(data)

plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])

plt.title("Multiple Box Plot Comparison")

plt.show()