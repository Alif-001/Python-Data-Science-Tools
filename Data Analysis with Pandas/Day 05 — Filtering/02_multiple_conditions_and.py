# =========================================
# Multiple Conditions (AND)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 AND condition মানে: দুইটা condition true হতে হবে

# 👉 উদাহরণ: Age > 25 AND Salary > 30000
filtered = df[(df['Age'] > 25) & (df['Salary'] > 30000)]

print(filtered)

# 👉 important:
# AND ব্যবহার করতে হলে & (ampersand) ব্যবহার করতে হয়
# প্রতিটি condition () এর ভিতরে দিতে হয়

# 👉 another example:
print(df[(df['City'] == 'Dhaka') & (df['Age'] > 20)])