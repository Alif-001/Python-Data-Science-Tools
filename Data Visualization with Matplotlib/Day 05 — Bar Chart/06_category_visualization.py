import matplotlib.pyplot as plt

"""
CATEGORY VISUALIZATION
----------------------
Used in real analytics dashboards.
"""

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [300, 150, 500, 200]

plt.bar(categories, expenses, color="purple")

plt.title("Monthly Expenses")
plt.xlabel("Categories")
plt.ylabel("Amount")

plt.show()