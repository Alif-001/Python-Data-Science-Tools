# =========================================
# Practice Filtering Examples
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 1. Dhaka city এর মানুষ
print(df[df['City'] == 'Dhaka'])

# 👉 2. Age 25 এর নিচে
print(df[df['Age'] < 25])

# 👉 3. Salary between 25000 - 40000
print(df[(df['Salary'] >= 25000) & (df['Salary'] <= 40000)])

# 👉 4. Highest earners (Salary > 35000)
print(df[df['Salary'] > 35000])

# 👉 5. Dhaka OR Khulna city
print(df[(df['City'] == 'Dhaka') | (df['City'] == 'Khulna')])

# 👉 summary:
# filtering = real-world data selection tool