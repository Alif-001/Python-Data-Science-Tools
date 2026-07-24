# =========================================
# Load CSV File in Pandas
# =========================================

import pandas as pd

# 👉 CSV কী?
# - Comma Separated Values
# - Excel এর simple text version

# 👉 CSV file load করা
# (ধরা যাক file same folder এ আছে)
df = pd.read_csv("data.csv")

# 👉 প্রথম কয়েকটা row print করা
print(df)

# 👉 যদি file অন্য folder এ থাকে:
# df = pd.read_csv("folder_name/data.csv")

# 👉 summary:
# read_csv() = CSV file load করার function