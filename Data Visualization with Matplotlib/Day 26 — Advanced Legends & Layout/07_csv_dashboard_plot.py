import pandas as pd
import matplotlib.pyplot as plt

"""
CSV DASHBOARD VISUALIZATION
---------------------------
Real-world multi-line dashboard plot.
"""

df = pd.read_csv("sales_multi_product.csv")

plt.figure(figsize=(10, 6))

# Plot multiple product lines
plt.plot(df["day"], df["product_A"], label="Product A")
plt.plot(df["day"], df["product_B"], label="Product B")
plt.plot(df["day"], df["product_C"], label="Product C")

# Legend customization
plt.legend(
    loc="upper left",
    title="Products",
    fontsize=10
)

plt.title("Sales Dashboard (Multi Product)")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.grid(True)

plt.show()