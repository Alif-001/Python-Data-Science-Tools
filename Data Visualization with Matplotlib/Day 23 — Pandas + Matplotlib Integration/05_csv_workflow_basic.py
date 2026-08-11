import pandas as pd
import matplotlib.pyplot as plt

"""
CSV VISUALIZATION WORKFLOW
-------------------------
Real-world workflow:
1. Load CSV
2. Clean / understand data
3. Plot directly
"""

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Show first rows
print(df.head())

# Plot directly
df.plot(x="date", y="sales", marker="o")

plt.title("CSV Based Plot")
plt.xticks(rotation=45)

plt.show()