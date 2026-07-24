# =========================================
# lambda function - quick function
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 salary category তৈরি করা

df['Salary_Category'] = df['Salary'].apply(
    lambda x: "High" if x > 35000 else "Low"
)

print(df)

# 👉 explanation:
# if-else logic ব্যবহার করা যায়