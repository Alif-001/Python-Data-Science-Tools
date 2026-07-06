import numpy as np

# =========================
# Real ML scenario: safe data copy
# =========================

data = np.array([10, 20, 30, 40, 50])

# model training data (copy required)
train_data = data.copy()

# normalization (safe on copy)
train_data = train_data / 10

print("Original data:", data)
print("Training data:", train_data)

# =========================
# Why copy important?
# - original dataset must not change
# - reproducibility needed in ML
# =========================