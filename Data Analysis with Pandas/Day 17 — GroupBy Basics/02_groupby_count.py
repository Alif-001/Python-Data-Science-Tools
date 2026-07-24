# =========================================
# Count per Group
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 প্রতি department এ কয়জন আছে
count = df.groupby('Department')['Name'].count()

print(count)

# 👉 explanation:
# IT → 3
# HR → 2
# Finance → 2