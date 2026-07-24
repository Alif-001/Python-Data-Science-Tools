# =========================================
# Real-world String Cleaning
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: lowercase all emails
df['Email'] = df['Email'].str.lower()

# 👉 Step 2: remove spaces (if any)
df['Email'] = df['Email'].str.strip()

# 👉 Step 3: check gmail users
gmail_users = df[df['Email'].str.contains("gmail")]

# 👉 Step 4: split email
df[['Username', 'Domain']] = df['Email'].str.split('@', expand=True)

print("Clean Data:")
print(df)

print("\nGmail Users:")
print(gmail_users)

# 👉 summary:
# string cleaning = standardization + filtering + parsing