# =========================================
# Real-world Sorting + Ranking
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Top earners (descending salary)
top_earners = df.sort_values(by='Salary', ascending=False)

print("Top Earners:")
print(top_earners)

# 👉 Top students by marks
top_students = df.sort_values(by='Marks', ascending=False)

print("\nTop Students:")
print(top_students)

# 👉 ranking marks
df['Marks_Rank'] = df['Marks'].rank(ascending=False)

print("\nWith Ranking:")
print(df)

# 👉 insight
print("\nBest Student:")
print(df.loc[df['Marks'].idxmax()])