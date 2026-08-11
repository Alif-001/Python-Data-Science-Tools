import pandas as pd
import matplotlib.pyplot as plt

"""
REAL SCIENTIFIC DATA ANALYSIS
----------------------------
We analyze experiment data.
"""

df = pd.read_csv("experiment_data.csv")

plt.figure(figsize=(10, 5))

# Temperature trend
plt.plot(df["time"], df["temperature"], marker="o", label="Temperature")

# Pressure trend
plt.plot(df["time"], df["pressure"], marker="o", label="Pressure")

plt.title("Scientific Experiment Analysis")
plt.xlabel("Time")
plt.ylabel("Values")

plt.legend()
plt.grid(True)

plt.show()