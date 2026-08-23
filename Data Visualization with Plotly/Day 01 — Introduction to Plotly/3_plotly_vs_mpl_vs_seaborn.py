# ==========================
# PLOTLY VS OTHER LIBRARIES
# ==========================

"""
We compare 3 popular visualization libraries:

1. Matplotlib
2. Seaborn
3. Plotly
"""

# --------------------------
# 1. Matplotlib (static)
# --------------------------
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Matplotlib (Static Plot)")
plt.show()

# Problem:
# - No zoom
# - No hover
# - Not interactive

# --------------------------
# 2. Seaborn (beautiful but still static)
# --------------------------
import seaborn as sns

tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn (Statistical Plot)")
plt.show()

# Good for:
# - Statistics
# - Quick EDA

# --------------------------
# 3. Plotly (interactive)
# --------------------------
import plotly.express as px

fig = px.bar(
    tips,
    x="day",
    y="total_bill",
    title="Plotly (Interactive Plot)"
)

fig.show()

"""
Plotly advantages:

✔ Zoom in/out
✔ Hover details
✔ Interactive tooltips
✔ Web-ready charts
✔ Dashboard support
"""