# =========================================
# Multiple Group + Sum
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 total salary per Department + City
result = df.groupby(['Department', 'City'])['Salary'].sum()

print(result)

# 👉 explanation:
# দুইটা column combine করে aggregation