# 08_final_missing_data_story.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# FINAL STORY: DATA QUALITY VIEW

# --------------------------------------------

plt.figure(figsize=(6, 4))

sns.heatmap(
df.isnull(),
cmap="YlOrRd",
cbar=False
)

plt.title("Where is My Data Missing?")
plt.xlabel("Features")
plt.ylabel("Students")

plt.show()

# --------------------------------------------

# INSIGHT:

# - instantly shows dataset quality

# --------------------------------------------
