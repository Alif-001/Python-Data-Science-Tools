# =========================================
# Categorical Grouping
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Marks → grade বানানো

df['Grade'] = pd.cut(
    df['Marks'],
    bins=[70, 80, 90, 100],
    labels=['C', 'B', 'A']
)

print(df)

# 👉 explanation:
# marks range → category (grade)