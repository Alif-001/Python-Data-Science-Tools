# =========================================
# Crosstab with Values (sum)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Salary sum per Department & City
ct = pd.crosstab(
    df['Department'],
    df['City'],
    values=df['Salary'],
    aggfunc='sum'
)

print(ct)

# 👉 explanation:
# শুধু count না, value-based summary করা যায়