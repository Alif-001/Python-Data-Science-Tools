# 02_all_plots_revision.py

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# --------------------------------------------

# 1. DISTRIBUTION

# --------------------------------------------

sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution Plot")
plt.show()

# --------------------------------------------

# 2. RELATIONSHIP

# --------------------------------------------

sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Scatter Plot")
plt.show()

# --------------------------------------------

# 3. CATEGORICAL

# --------------------------------------------

sns.barplot(data=df, x="day", y="total_bill")
plt.title("Bar Plot")
plt.show()

# --------------------------------------------

# 4. BOX PLOT

# --------------------------------------------

sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Box Plot")
plt.show()

# --------------------------------------------

# 5. VIOLIN PLOT

# --------------------------------------------

sns.violinplot(data=df, x="day", y="total_bill")
plt.title("Violin Plot")
plt.show()

# --------------------------------------------

# 6. HEATMAP

# --------------------------------------------

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Heatmap")
plt.show()

# --------------------------------------------

# KEY IDEA:

# - revise core plots

# --------------------------------------------
