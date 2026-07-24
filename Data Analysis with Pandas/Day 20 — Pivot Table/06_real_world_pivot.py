# =========================================
# Real-world Pivot Table Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 full analysis pivot
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='City',
    aggfunc=['mean', 'sum'],
    fill_value=0
)

print("Pivot Table:\n", pivot)

# 👉 insight
print("\nHighest Average Salary Department:")
print(pivot['mean'].mean(axis=1).idxmax())

# 👉 explanation:
# pivot = business reporting tool