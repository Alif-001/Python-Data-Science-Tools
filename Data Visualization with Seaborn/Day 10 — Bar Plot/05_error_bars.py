# 05_error_bars.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ERROR BARS

# --------------------------------------------

# Show variability in data

sns.barplot(
data=tips,
x="day",
y="total_bill",
errorbar="ci"   # confidence interval
)

plt.title("Bar Plot with Confidence Interval")
plt.show()

# --------------------------------------------

# OTHER OPTIONS:

# errorbar="sd" → standard deviation

# errorbar=None → no error bars

# --------------------------------------------

# Without error bars:

sns.barplot(
data=tips,
x="day",
y="total_bill",
errorbar=None
)

plt.title("No Error Bars")
plt.show()
