# =========================================
# astype() - Change Data Type
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Age string → integer
df['Age'] = df['Age'].astype(int)

# 👉 Salary string → integer
df['Salary'] = df['Salary'].astype(int)

print(df.dtypes)

# 👉 explanation:
# astype() = manual type conversion
# useful when data loaded as string