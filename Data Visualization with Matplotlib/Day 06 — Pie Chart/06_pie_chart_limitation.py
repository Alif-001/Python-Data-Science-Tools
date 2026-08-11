import matplotlib.pyplot as plt

"""
PIE CHART LIMITATIONS
---------------------
- Hard to compare similar values
- Not good for many categories
- Not good for precise analysis
"""

labels = ["A", "B", "C", "D", "E", "F", "G"]
values = [10, 15, 20, 5, 25, 10, 15]

plt.pie(values, labels=labels, autopct="%1.1f%%")

plt.title("Too Many Categories = Hard to Read ❌")

plt.show()