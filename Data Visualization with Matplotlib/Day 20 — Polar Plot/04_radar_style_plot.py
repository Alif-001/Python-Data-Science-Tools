import numpy as np
import matplotlib.pyplot as plt

"""
RADAR STYLE VISUALIZATION
-------------------------
Used for comparing categories:
Example: student performance, skills, etc.
"""

# Categories
labels = ["Speed", "Power", "Accuracy", "Stamina", "Skill"]

# Values for one person
values = [4, 3, 5, 2, 4]

# Close the circle
values += values[:1]

# Angles
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

plt.subplot(111, projection='polar')

plt.plot(angles, values)
plt.fill(angles, values, alpha=0.3)

plt.xticks(angles[:-1], labels)

plt.title("Radar Style Plot")

plt.show()