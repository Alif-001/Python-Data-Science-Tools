import matplotlib.pyplot as plt

"""
QUARTILES EXPLAINED VISUALLY
----------------------------
Box plot automatically shows:
- Q1 (25%)
- Median (50%)
- Q3 (75%)
"""

data = [10, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90]

plt.boxplot(data)

plt.title("Box Plot with Quartiles")

plt.show()