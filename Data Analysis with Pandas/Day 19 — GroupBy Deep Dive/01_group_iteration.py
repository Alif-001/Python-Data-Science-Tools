# =========================================
# Iteration over Groups
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 group তৈরি
grouped = df.groupby('Department')

# 👉 প্রতিটি group iterate করা
for dept, group in grouped:
    print("Department:", dept)
    print(group)
    print("-" * 30)

# 👉 explanation:
# dept = group name (IT, HR, etc.)
# group = সেই group এর data