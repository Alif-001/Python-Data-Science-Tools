import pandas as pd
import matplotlib.pyplot as plt

"""
GROUPED PLOTTING
----------------
We compare categories (like products or cities).
"""

data = {
    "day": [1, 2, 3, 4, 5],
    "A_product": [100, 120, 140, 130, 150],
    "B_product": [90, 110, 130, 120, 160]
}

df = pd.DataFrame(data)

df.plot(x="day", y=["A_product", "B_product"], marker="o")

plt.title("Grouped Product Sales")

plt.show()