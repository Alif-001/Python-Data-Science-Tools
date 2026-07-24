# =========================================
# Multiple Conditions (OR)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 OR condition মানে: যেকোনো একটা true হলেই হবে

# 👉 উদাহরণ: Age > 28 OR Salary > 40000
filtered = df[(df['Age'] > 28) | (df['Salary'] > 40000)]

print(filtered)

# 👉 important:
# OR ব্যবহার করতে | (pipe) ব্যবহার হয়

# 👉 example:
print(df[(df['City'] == 'Dhaka') | (df['City'] == 'Sylhet')])