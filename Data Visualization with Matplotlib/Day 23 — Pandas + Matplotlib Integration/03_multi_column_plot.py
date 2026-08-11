import pandas as pd
import matplotlib.pyplot as plt

"""
MULTI COLUMN PLOTTING
---------------------
We can plot multiple features at once.
"""

data = {
    "day": [1, 2, 3, 4, 5],
    "sales": [100, 120, 150, 130, 170],
    "profit": [30, 40, 50, 45, 60]
}

df = pd.DataFrame(data)

df.plot(x="day", y=["sales", "profit"], marker="o")

plt.title("Sales vs Profit Comparison")

plt.show()