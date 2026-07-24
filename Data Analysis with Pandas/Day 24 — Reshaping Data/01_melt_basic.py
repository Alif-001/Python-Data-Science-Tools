# =========================================
# melt() - Wide to Long format
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 melt = columns → rows এ convert করা

melted = pd.melt(
    df,
    id_vars=['Name'],          # fixed column
    var_name='Subject',       # নতুন column name
    value_name='Marks'        # values column
)

print(melted)

# 👉 explanation:
# wide data → long format (analysis friendly)