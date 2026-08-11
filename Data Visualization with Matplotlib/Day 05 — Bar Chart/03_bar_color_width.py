import matplotlib.pyplot as plt

"""
COLOR + WIDTH CONTROL
---------------------
We can customize bar appearance.
"""

products = ["A", "B", "C", "D"]
sales = [20, 35, 30, 50]

plt.bar(
    products,
    sales,
    color="orange",   # bar color
    width=0.5         # bar thickness
)

plt.title("Bar Chart with Color and Width")

plt.show()