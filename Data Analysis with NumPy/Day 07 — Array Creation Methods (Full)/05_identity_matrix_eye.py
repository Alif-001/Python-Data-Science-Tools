import numpy as np

# =========================
# Identity Matrix (eye)
# =========================

# Identity matrix → diagonal 1, rest 0
I = np.eye(4)

print("Identity Matrix (4x4):\n", I)

# non-square identity-like matrix
I2 = np.eye(3, 5)

print("\n3x5 Eye Matrix:\n", I2)

# diagonal shift (k parameter)
I3 = np.eye(4, k=1)

print("\nShifted diagonal (k=1):\n", I3)