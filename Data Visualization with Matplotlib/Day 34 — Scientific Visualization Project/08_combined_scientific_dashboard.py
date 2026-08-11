import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
SCIENTIFIC DASHBOARD (FULL PROJECT)
-----------------------------------
Combines:
- math
- physics
- real data
"""

df = pd.read_csv("experiment_data.csv")

time = df["time"]

plt.figure(figsize=(12, 8))

# ---- Temperature ----
plt.subplot(2, 2, 1)
plt.plot(time, df["temperature"], color="red")
plt.title("Temperature Trend")

# ---- Pressure ----
plt.subplot(2, 2, 2)
plt.plot(time, df["pressure"], color="blue")
plt.title("Pressure Trend")

# ---- Mathematical function ----
plt.subplot(2, 2, 3)
x = np.linspace(-5, 5, 100)
plt.plot(x, x**2)
plt.title("Mathematical Model (x²)")

# ---- Noise simulation ----
plt.subplot(2, 2, 4)
signal = np.sin(x)
noise = np.random.normal(0, 0.2, 100)
plt.plot(x, signal + noise)
plt.title("Noisy Signal")

plt.tight_layout()
plt.show()