# =========================================
# std() - Standard Deviation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 standard deviation = data কতটা spread হয়েছে
print("Salary STD:", df['Salary'].std())

# 👉 explanation:
# low std → data close
# high std → data spread বেশি