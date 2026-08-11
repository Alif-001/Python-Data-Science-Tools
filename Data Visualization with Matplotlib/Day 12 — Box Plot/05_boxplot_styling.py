import matplotlib.pyplot as plt

"""
BOX PLOT STYLING
----------------
We can customize appearance.
"""

data = [20, 25, 30, 35, 40, 45, 50, 55, 60]

plt.boxplot(
    data,
    patch_artist=True,  # fills color
    boxprops=dict(facecolor="lightblue"),
    medianprops=dict(color="red")
)

plt.title("Styled Box Plot")

plt.show()