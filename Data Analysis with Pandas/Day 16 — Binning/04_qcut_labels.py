# =========================================
# qcut() with labels
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

labels = ['Low', 'Medium', 'High']

df['Salary_Level'] = pd.qcut(df['Salary'], q=3, labels=labels)

print(df)

# 👉 explanation:
# lowest salaries → Low
# highest salaries → High