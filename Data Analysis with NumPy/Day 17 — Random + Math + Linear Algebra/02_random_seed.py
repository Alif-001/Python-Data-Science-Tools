import numpy as np

# -----------------------------------
# Seed → reproducible randomness
# -----------------------------------

np.random.seed(42)

print(np.random.rand(3))
# same output every time run করলে
# কারণ seed fixed করা হয়েছে

# ML experiments এ reproducibility খুব important