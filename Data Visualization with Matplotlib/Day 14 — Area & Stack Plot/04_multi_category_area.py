import matplotlib.pyplot as plt

"""
MULTI-CATEGORY AREA CHART
-------------------------
Shows multiple trends together.
"""

months = [1, 2, 3, 4, 5]

product_a = [3, 4, 5, 6, 7]
product_b = [2, 3, 4, 5, 6]
product_c = [1, 2, 3, 4, 5]

plt.stackplot(
    months,
    product_a,
    product_b,
    product_c,
    labels=["Product A", "Product B", "Product C"],
    alpha=0.6
)

plt.title("Product Performance Over Time")
plt.legend()

plt.show()