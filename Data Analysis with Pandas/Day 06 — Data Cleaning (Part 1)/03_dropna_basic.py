# =========================================
# dropna() - remove missing values
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 dropna() = যেসব row তে NaN আছে, সেগুলো remove করে

cleaned_df = df.dropna()

print(cleaned_df)

# 👉 explanation:
# যেসব row এ 1টা NaN থাকলেও পুরো row delete হয়ে যাবে

# 👉 original data unchanged থাকে
print(df)