import matplotlib.pyplot as plt
import numpy as np

"""
VIOLIN STYLING
--------------
We can customize appearance.
"""

data = np.random.normal(50, 10, 100)

vp = plt.violinplot(data, showmeans=True, showmedians=True)

# Color customization
for body in vp['bodies']:
    body.set_facecolor("lightblue")
    body.set_edgecolor("black")
    body.set_alpha(0.7)

plt.title("Styled Violin Plot")

plt.show()