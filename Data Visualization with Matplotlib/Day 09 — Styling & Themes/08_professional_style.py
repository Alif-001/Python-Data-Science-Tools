import matplotlib.pyplot as plt

"""
PROFESSIONAL VISUALIZATION STYLE
--------------------------------
This is how real dashboards look.
"""

plt.style.use("seaborn-v0_8")

x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 40]

plt.figure(figsize=(8, 4))

plt.plot(x, y, color="#1f77b4", linewidth=3, marker="o")

plt.title("Professional Chart", fontsize=16, fontweight="bold")
plt.xlabel("Time", fontsize=12)
plt.ylabel("Value", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()