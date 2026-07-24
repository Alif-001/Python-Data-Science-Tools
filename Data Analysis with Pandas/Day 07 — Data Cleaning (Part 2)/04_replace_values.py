# =========================================
# replace() - Value Replacement
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 replace() ব্যবহার করে specific value change করা যায়

# 👉 Dhaka → DHAKA (uppercase)
df_replaced = df.replace("Dhaka", "DHAKA")

print(df_replaced)

# 👉 multiple value replace
df_replaced2 = df.replace({
    "Sylhet": "SYL",
    "Khulna": "KHU"
})

print(df_replaced2)

# 👉 numeric replace example
df_replaced3 = df.replace(25000, 99999)

print(df_replaced3)

# 👉 summary:
# replace = exact value change