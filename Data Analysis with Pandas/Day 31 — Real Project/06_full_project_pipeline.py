# =========================================
# FULL END-TO-END PIPELINE
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

# STEP 1: CLEANING
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# STEP 2: FEATURE ENGINEERING
df['Total_Pay'] = df['Salary'] + df['Bonus']

df['Performance'] = df['Score'].apply(
    lambda x: 'Excellent' if x >= 90 else ('Good' if x >= 80 else 'Average')
)

# STEP 3: GROUP ANALYSIS
group = df.groupby('Department')['Total_Pay'].mean()

# STEP 4: PIVOT VIEW
pivot = pd.pivot_table(
    df,
    values='Total_Pay',
    index='Department',
    columns='City',
    aggfunc='mean',
    fill_value=0
)

print("Clean Data:\n", df)
print("\nGroup Analysis:\n", group)
print("\nPivot Table:\n", pivot)

# 👉 explanation:
# এটা full data science pipeline