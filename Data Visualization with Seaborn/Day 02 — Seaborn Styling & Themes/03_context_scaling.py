# 03_context_scaling.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONTEXT SCALING

# --------------------------------------------

# This controls SIZE of everything:

# - fonts

# - labels

# - lines

# - overall readability

# --------------------------------------------

contexts = ["paper", "notebook", "talk", "poster"]

for context in contexts:

```
sns.set_theme(context=context)

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title(f"Context: {context}")
plt.show()
```

# --------------------------------------------

# MEANING:

# --------------------------------------------

# paper   → small plots (research paper)

# notebook→ default Jupyter style

# talk    → presentation slides

# poster  → large posters

# --------------------------------------------
