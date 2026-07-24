# =========================================
# Single Condition Filtering
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Filtering মানে: condition অনুযায়ী data বের করা

# 👉 উদাহরণ: Age > 25 যাদের
filtered = df[df['Age'] > 25]

print(filtered)

# 👉 explanation:
# df['Age'] > 25 → True/False তৈরি করে
# True যেগুলো, শুধু সেগুলো রাখে

# 👉 আরেকটা example: Salary > 30000
print(df[df['Salary'] > 30000])