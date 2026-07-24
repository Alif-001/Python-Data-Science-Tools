# =========================================
# fillna() - Column Specific Values
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 different column এ different value fill করা

df_filled = df.fillna({
    'Age': df['Age'].mean(),   # Age এর missing → average
    'City': 'Unknown',         # City missing → Unknown
    'Salary': df['Salary'].median()  # Salary → median
})

print(df_filled)

# 👉 explanation:
# real-world data cleaning এ এই method বেশি ব্যবহার হয়