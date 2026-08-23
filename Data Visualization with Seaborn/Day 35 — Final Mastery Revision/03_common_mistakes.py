# 03_common_mistakes.py

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# --------------------------------------------

# MISTAKE 1: TOO MUCH INFORMATION

# --------------------------------------------

sns.scatterplot(
data=df,
x="total_bill",
y="tip",
hue="day",
style="sex",
size="size"
)

plt.title("Too cluttered plot")
plt.show()

# --------------------------------------------

# MISTAKE 2: WRONG PLOT TYPE

# --------------------------------------------

sns.lineplot(data=df, x="total_bill", y="tip")
plt.title("Wrong use of line plot")
plt.show()

# --------------------------------------------

# LESSON:

# - avoid overcomplication

# - choose correct plot type

# --------------------------------------------
