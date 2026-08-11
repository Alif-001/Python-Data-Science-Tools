import pandas as pd
import matplotlib.pyplot as plt

"""
DAY 23 - PANDAS + MATPLOTLIB INTEGRATION
---------------------------------------
We directly plot from Pandas DataFrame.
No need to manually extract lists.
"""

# Create simple DataFrame
data = {
    "day": [1, 2, 3, 4, 5],
    "sales": [100, 120, 150, 130, 170]
}

df = pd.DataFrame(data)

# Pandas has built-in plotting (uses matplotlib internally)
df.plot(x="day", y="sales", marker="o")

plt.title("Basic DataFrame Plot")
plt.show()