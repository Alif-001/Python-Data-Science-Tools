# =========================================
# Real-world DateTime Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 Step 1: extract year
df['Year'] = df['JoinDate'].dt.year

# 👉 Step 2: group by year
yearly_salary = df.groupby('Year')['Salary'].mean()

print("Yearly Average Salary:\n", yearly_salary)

# 👉 Step 3: latest joiners
latest = df.sort_values(by='JoinDate', ascending=False)

print("\nLatest Employees:\n", latest)

# 👉 explanation:
# datetime = time-based analytics core