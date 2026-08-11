import pandas as pd
import matplotlib.pyplot as plt

"""
INDEX PLOTTING
--------------
We use DataFrame index as X-axis automatically.
"""

sales = [100, 120, 90, 150, 180]

df = pd.DataFrame({
    "sales": sales
})

# Index becomes X-axis automatically
df.plot(marker="o")

plt.title("Index Based Plot")
plt.xlabel("Index (Auto)")
plt.ylabel("Sales")

plt.show()