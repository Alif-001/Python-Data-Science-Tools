# =========================================
# Scaling using apply()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 custom scaling function
def min_max(col):
    return (col - col.min()) / (col.max() - col.min())

# 👉 apply on multiple columns
df[['Age', 'Salary', 'Marks']] = df[['Age', 'Salary', 'Marks']].apply(min_max)

print(df)

# 👉 explanation:
# apply() দিয়ে reusable scaling করা যায়