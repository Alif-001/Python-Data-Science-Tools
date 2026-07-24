# =========================================
# sort_values() with Multiple Columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Age + Salary অনুযায়ী sort
sorted_df = df.sort_values(by=['Age', 'Salary'])

print(sorted_df)

# 👉 mixed order (Age asc, Salary desc)
sorted_mixed = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])

print("\nMixed Sorting:")
print(sorted_mixed)

# 👉 explanation:
# multiple column দিয়ে priority sorting করা যায়