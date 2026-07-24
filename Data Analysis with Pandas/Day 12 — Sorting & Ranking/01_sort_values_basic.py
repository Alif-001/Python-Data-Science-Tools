# =========================================
# sort_values() - Column Based Sorting
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Salary অনুযায়ী ascending sort (default)
sorted_df = df.sort_values(by='Salary')

print(sorted_df)

# 👉 descending sort
sorted_desc = df.sort_values(by='Salary', ascending=False)

print("\nDescending:")
print(sorted_desc)

# 👉 explanation:
# sort_values() = column ভিত্তিক sort