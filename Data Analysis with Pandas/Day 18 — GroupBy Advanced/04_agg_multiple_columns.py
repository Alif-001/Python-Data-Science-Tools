# =========================================
# agg() on multiple columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 different column এ different function
result = df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Age': ['min', 'max']
})

print(result)

# 👉 explanation:
# dictionary দিয়ে control করা যায়