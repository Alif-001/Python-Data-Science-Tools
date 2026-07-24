# =========================================
# transform() with custom function
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 salary difference from group mean
df['Diff_From_Avg'] = df['Salary'] - df.groupby('Department')['Salary'].transform('mean')

print(df)

# 👉 explanation:
# প্রতিটি row → group average এর সাথে compare