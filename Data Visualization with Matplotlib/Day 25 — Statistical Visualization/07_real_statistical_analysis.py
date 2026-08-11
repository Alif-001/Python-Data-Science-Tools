import pandas as pd
import matplotlib.pyplot as plt

"""
REAL STATISTICAL ANALYSIS
-------------------------
We compute mean, median and visualize.
"""

df = pd.read_csv("student_marks.csv")

# Calculate average marks
df["average"] = df[["math", "science", "english"]].mean(axis=1)

# Mean of averages
mean_value = df["average"].mean()

# Median of averages
median_value = df["average"].median()

# Plot
plt.plot(df["student"], df["average"], marker="o", label="Average Marks")

# Mean line
plt.axhline(mean_value, color="red", linestyle="--", label="Mean")

# Median line
plt.axhline(median_value, color="green", linestyle="--", label="Median")

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.legend()
plt.grid(True)

plt.show()