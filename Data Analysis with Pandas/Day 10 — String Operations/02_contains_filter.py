# =========================================
# contains() - search inside text
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 যাদের email gmail.com আছে তাদের খুঁজবো
gmail_users = df[df['Email'].str.contains("gmail")]

print(gmail_users)

# 👉 explanation:
# contains() = text search tool
# real-world: filter users, logs, emails