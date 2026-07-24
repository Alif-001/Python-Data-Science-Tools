# =========================================
# Custom Aggregation Function
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 custom function define
def salary_range(x):
    return x.max() - x.min()

# 👉 apply custom function
result = df.groupby('Department')['Salary'].agg(salary_range)

print(result)

# 👉 explanation:
# custom logic ব্যবহার করা যায়