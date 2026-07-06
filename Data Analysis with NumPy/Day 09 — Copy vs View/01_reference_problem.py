import numpy as np

# =========================
# Python list example (reference behavior)
# =========================

a = [1, 2, 3]
b = a   # same memory reference

b[0] = 100  # change b → a ও change হবে

print("a:", a)
print("b:", b)

# =========================
# Problem:
# Python list = reference based (dangerous sometimes)
# =========================