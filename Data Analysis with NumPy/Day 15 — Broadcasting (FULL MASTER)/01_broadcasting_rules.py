import numpy as np

# -----------------------------------
# Broadcasting Rules (Core Concept)
# -----------------------------------

# Rule 1: Dimensions match হলে operation হয়
# Rule 2: One side যদি 1 হয় → expand হয়ে যায়
# Rule 3: Small array automatically stretch হয়

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
# [11 22 33]

# এখানে shape একই → direct operation