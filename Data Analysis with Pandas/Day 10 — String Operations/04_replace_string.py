# =========================================
# replace() - string replacement
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 gmail.com কে gmail.org বানানো
df['Email'] = df['Email'].str.replace("gmail.com", "gmail.org")

print(df)

# 👉 City replace example
df['City'] = df['City'].str.replace("Dhaka", "DHAKA")

print(df)

# 👉 explanation:
# replace() = exact text change