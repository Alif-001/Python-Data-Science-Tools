# =========================================
# Performance Comparison Idea
# =========================================

import pandas as pd
import time

df = pd.read_csv("data.csv")

# 👉 slow method
start = time.time()
df['A'] = df['Value'].apply(lambda x: x + 10)
end = time.time()

print("Apply time:", end - start)

# 👉 fast method
start = time.time()
df['B'] = df['Value'] + 10
end = time.time()

print("Vectorized time:", end - start)

# 👉 explanation:
# direct operation অনেক faster