# =========================================
# Deep level selection
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df = df.set_index(['Country', 'City', 'Department'])

# 👉 exact department access
print(df.loc[('Bangladesh', 'Dhaka', 'IT')])

# 👉 explanation:
# সব level specify করলে exact row পাওয়া যায়