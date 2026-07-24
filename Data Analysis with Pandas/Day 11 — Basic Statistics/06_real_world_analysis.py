# =========================================
# Real-world Data Analysis Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 average salary
avg_salary = df['Salary'].mean()

# 👉 highest marks
max_marks = df['Marks'].max()

# 👉 lowest age
min_age = df['Age'].min()

# 👉 total salary
total_salary = df['Salary'].sum()

print("Average Salary:", avg_salary)
print("Highest Marks:", max_marks)
print("Lowest Age:", min_age)
print("Total Salary:", total_salary)

# 👉 simple insight
print("\nInsight:")
if avg_salary > 30000:
    print("Overall salary is good")
else:
    print("Salary is relatively low")