import numpy as np

# -----------------------------------
# Random numbers generation (NumPy)
# -----------------------------------

# 0 to 1 এর মধ্যে random float
print(np.random.rand(3))
# example: [0.23 0.91 0.44]

# random integer (start, end)
print(np.random.randint(1, 10, 5))
# 1 থেকে 9 এর মধ্যে 5টা সংখ্যা

# uniform distribution (range float)
print(np.random.uniform(10, 20, 5))
# 10 থেকে 20 এর মধ্যে float values