# 04_color_palettes.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# COLOR PALETTES

# --------------------------------------------

# Helps in making data visually meaningful

# --------------------------------------------

palettes = [
"deep",
"muted",
"bright",
"pastel",
"dark",
"colorblind"
]

for palette in palettes:

```
sns.set_theme(palette=palette)

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"   # category coloring
)

plt.title(f"Palette: {palette}")
plt.show()
```

# --------------------------------------------

# TIP:

# colorblind palette = best for accessibility

# --------------------------------------------
