# =========================================
# melt() with multiple id columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple id columns (example add Age)
df['Age'] = [22, 25, 28, 21]

melted = pd.melt(
    df,
    id_vars=['Name', 'Age'],
    var_name='Subject',
    value_name='Marks'
)

print(melted)

# 👉 explanation:
# multiple identity columns রাখা যায়