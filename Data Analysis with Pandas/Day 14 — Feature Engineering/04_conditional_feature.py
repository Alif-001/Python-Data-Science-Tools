# =========================================
# Conditional Feature Engineering
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 performance category

df['Performance'] = df['Marks'].apply(
    lambda x: "Excellent" if x >= 90 else (
        "Good" if x >= 80 else "Average"
    )
)

print(df)

# 👉 explanation:
# condition based feature = খুব common real-world case