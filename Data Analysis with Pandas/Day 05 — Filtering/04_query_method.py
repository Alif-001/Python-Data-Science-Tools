# =========================================
# query() method (very clean filtering)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 query() দিয়ে filtering আরও সহজ হয়

# 👉 example: Age > 25
print(df.query("Age > 25"))

# 👉 example: Salary > 30000
print(df.query("Salary > 30000"))

# 👉 multiple condition (AND)
print(df.query("Age > 25 and Salary > 30000"))

# 👉 multiple condition (OR)
print(df.query("City == 'Dhaka' or City == 'Sylhet'"))

# 👉 summary:
# query() = readable filtering syntax