# =========================================
# Row-wise apply (axis=1)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 function define
def grade(row):
    if row['Marks'] >= 90:
        return "A"
    elif row['Marks'] >= 80:
        return "B"
    else:
        return "C"

# 👉 row-wise apply
df['Grade'] = df.apply(grade, axis=1)

print(df)

# 👉 explanation:
# axis=1 → row-wise
# row = পুরো row access করা যায়