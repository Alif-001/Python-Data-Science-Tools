# =========================================
# Select data by first level index
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df = df.set_index(['Country', 'City', 'Department'])

# 👉 Bangladesh এর সব data
print(df.loc['Bangladesh'])

# 👉 explanation:
# top level index দিয়ে filter করা যায়