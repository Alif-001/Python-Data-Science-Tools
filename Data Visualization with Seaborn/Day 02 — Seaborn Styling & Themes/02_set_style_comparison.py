# 02_set_style_comparison.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# Available styles in seaborn:

# darkgrid, whitegrid, dark, white, ticks

# --------------------------------------------

styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

# Create multiple plots to compare styles

for style in styles:

```
sns.set_style(style)

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title(f"Style: {style}")
plt.show()
```

# --------------------------------------------

# KEY IDEA:

# --------------------------------------------

# - darkgrid → best for analysis

# - whitegrid → clean reports

# - dark → presentation style

# - white → minimal design

# - ticks → publication style

# --------------------------------------------
