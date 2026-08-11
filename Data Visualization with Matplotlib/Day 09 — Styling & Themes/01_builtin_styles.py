import matplotlib.pyplot as plt

"""
DAY 9 - STYLING & THEMES
------------------------
Matplotlib has built-in styles like:
- ggplot
- seaborn
- classic
"""

# See available styles
print(plt.style.available)

# Apply a built-in style
plt.style.use("ggplot")

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Built-in Style: ggplot")
plt.show()