# =========================================
# Arithmetic Operations on Columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple column ব্যবহার করে নতুন column

# 👉 Total Income = Salary + Bonus
df['Bonus'] = df['Salary'] * 0.10
df['Total_Income'] = df['Salary'] + df['Bonus']

print(df)

# 👉 another example:
# Marks percentage increase (curve)
df['Marks_Updated'] = df['Marks'] + 5

print(df)

# 👉 explanation:
# arithmetic operations = +, -, *, /