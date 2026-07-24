# =========================================
# Crosstab - Frequency Table
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Department vs City frequency table
ct = pd.crosstab(df['Department'], df['City'])

print(ct)

# 👉 explanation:
# কতজন কোন department + city তে আছে সেটা count করে