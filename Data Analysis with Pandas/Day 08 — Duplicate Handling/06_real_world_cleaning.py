# =========================================
# Real-world Duplicate Cleaning Strategy
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: check duplicates
print("Total duplicates:", df.duplicated().sum())

# 👉 Step 2: inspect duplicates
print("\nDuplicate rows:")
print(df[df.duplicated()])

# 👉 Step 3: remove duplicates safely
df_clean = df.drop_duplicates()

# 👉 Step 4: reset index (clean look)
df_clean = df_clean.reset_index(drop=True)

print("\nClean dataset:")
print(df_clean)

# 👉 summary:
# real project = detect → inspect → remove → reset index