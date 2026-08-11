import matplotlib.pyplot as plt

"""
DAY 12 - BOX PLOT
-----------------
Box plot shows:
- Median (middle value)
- Quartiles (Q1, Q3)
- Spread of data
- Outliers
"""

# Sample data (student marks)
marks = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Create box plot
plt.boxplot(marks)

plt.title("Basic Box Plot")
plt.ylabel("Marks")

plt.show()