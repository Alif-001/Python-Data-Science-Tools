import numpy as np

# -----------------------------------
# Real-world Use Cases
# -----------------------------------

# 1. Data normalization (ML important)
data = np.array([10, 20, 30, 40, 50])

mean = 20

# subtract mean (center data)
normalized = data - mean
print(normalized)
# [-10 0 10 20 30]

# -----------------------------------

# 2. Image brightness adjustment (Computer Vision idea)
image = np.array([
    [100, 150],
    [200, 250]
])

brightness = 50

print(image + brightness)
# brightness automatically apply

# -----------------------------------

# 3. Feature scaling (ML preprocessing)
features = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

scale = np.array([10, 100, 1000])

print(features * scale)