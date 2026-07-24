# ================================
# DataFrame Structure
# ================================

import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [80, 90, 85]
}

df = pd.DataFrame(data)

# 👉 rows & columns সংখ্যা
print(df.shape)
# output: (3, 2)
# 3 rows, 2 columns

# 👉 column names
print(df.columns)

# 👉 index (row number)
print(df.index)

# 👉 data types
print(df.dtypes)

# 👉 summary:
# rows = horizontal data
# columns = vertical data
# index = row labels