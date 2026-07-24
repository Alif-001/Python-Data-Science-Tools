# =========================================
# GroupBy Concept Introduction
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 groupby মানে:
# same category (Department) অনুযায়ী data group করা

grouped = df.groupby('Department')

print(grouped)

# 👉 explanation:
# এটা actual result না, এটা group object
# apply function করলে result পাওয়া যায়