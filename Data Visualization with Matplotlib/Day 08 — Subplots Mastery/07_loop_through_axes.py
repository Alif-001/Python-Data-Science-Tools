import matplotlib.pyplot as plt

"""
LOOP THROUGH AXES
-----------------
Useful when many plots exist.
"""

x = [1, 2, 3, 4]

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

plots = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
]

i = 0

for row in ax:
    for col in row:
        col.plot(x, plots[i])
        col.set_title(f"Plot {i+1}")
        i += 1

plt.tight_layout()
plt.show()