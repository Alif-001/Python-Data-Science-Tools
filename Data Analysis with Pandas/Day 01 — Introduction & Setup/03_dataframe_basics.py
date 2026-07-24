# ================================
# Pandas DataFrame (2D data)
# ================================

import pandas as pd

# 👉 DataFrame কী?
# - table (rows + columns)
# - Excel sheet এর মতো

# 👉 dictionary দিয়ে DataFrame তৈরি
data = {
    'Name': ['Rahim', 'Karim', 'Sakib'],
    'Age': [20, 22, 25],
    'City': ['Dhaka', 'Sylhet', 'Chittagong']
}

df = pd.DataFrame(data)

print(df)

# 👉 output:
# rows = 3 (Rahim, Karim, Sakib)
# columns = Name, Age, City

# 👉 specific column access
print(df['Name'])

# 👉 multiple column access
print(df[['Name', 'Age']])