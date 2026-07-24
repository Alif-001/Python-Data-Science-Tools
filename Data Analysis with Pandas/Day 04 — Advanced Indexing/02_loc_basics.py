# =========================================
# loc - Label Based Indexing
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 loc মানে: label / name / condition অনুযায়ী select

# 👉 default index (0,1,2...) থাকলেও loc ব্যবহার করা যায়
print(df.loc[0])

# 👉 multiple rows
print(df.loc[0:3])
# NOTE: loc এ শেষ index INCLUDED থাকে

# 👉 specific row + column
print(df.loc[0, 'Name'])

# 👉 multiple columns
print(df.loc[0, ['Name', 'City']])

# 👉 summary:
# loc = label based selection