# =========================================
# split() - text break into parts
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 email কে username & domain এ ভাগ করা

df[['Username', 'Domain']] = df['Email'].str.split('@', expand=True)

print(df)

# 👉 explanation:
# before: rahim@gmail.com
# after:
# Username = rahim
# Domain = gmail.com