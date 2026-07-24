# =========================================
# dropna() - column based control
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 যদি column-wise clean করতে চাই

# only drop rows where Salary is missing
clean_salary = df.dropna(subset=['Salary'])

print(clean_salary)

# 👉 multiple column check
clean_multiple = df.dropna(subset=['Age', 'City'])

print(clean_multiple)

# 👉 summary:
# subset = specific column based cleaning