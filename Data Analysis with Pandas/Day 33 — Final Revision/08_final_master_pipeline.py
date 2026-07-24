# =========================================
# FINAL MASTER PIPELINE (ALL-IN-ONE)
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

# STEP 1: CLEANING
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# STEP 2: FEATURE ENGINEERING
df['Total_Pay'] = df['Salary'] + df['Bonus']

df['Performance'] = df['Score'].apply(
    lambda x: 'Excellent' if x >= 90 else ('Good' if x >= 80 else 'Average')
)

# STEP 3: ANALYSIS
group = df.groupby('Department')['Total_Pay'].mean()

# STEP 4: INSIGHT
best_emp = df.loc[df['Total_Pay'].idxmax()]
best_dept = group.idxmax()

print("Dataset:\n", df)
print("\nDepartment Analysis:\n", group)
print("\nBest Employee:\n", best_emp)
print("\nBest Department:", best_dept)

# 👉 revision:
# full pipeline = real-world data science workflow