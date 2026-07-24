# =========================================
# Min-Max Scaling (0 to 1 range)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 formula:
# (x - min) / (max - min)

# 👉 Salary scaling
min_val = df['Salary'].min()
max_val = df['Salary'].max()

df['Salary_scaled'] = (df['Salary'] - min_val) / (max_val - min_val)

print(df)

# 👉 explanation:
# scaling → data same range এ আনা
# ML model এর জন্য important