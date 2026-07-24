# =========================================
# mean(), median(), mode()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 mean() = average value
print("Mean Age:", df['Age'].mean())

# 👉 median() = middle value (sorted data)
print("Median Salary:", df['Salary'].median())

# 👉 mode() = most frequent value
print("Mode Marks:")
print(df['Marks'].mode())

# 👉 explanation:
# mean → average
# median → middle point
# mode → most repeated value