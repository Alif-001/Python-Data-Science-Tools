# ================================
# Pandas Series (1D data structure)
# ================================

import pandas as pd

# 👉 Series কী?
# - 1D array এর মতো (list এর মতো)
# - index + value থাকে

# 👉 simple series তৈরি
data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)

# 👉 Output explanation:
# left side = index (0,1,2,3)
# right side = value (10,20,30,40)

# 👉 custom index ব্যবহার করা
s2 = pd.Series(data, index=['a', 'b', 'c', 'd'])

print(s2)

# 👉 value access করা
print(s2['a'])   # output: 10

# 👉 summary:
# Series = single column data