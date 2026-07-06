import numpy as np

# ML idea:
# dataset = (samples, features, time/extra dimension)

data = np.random.randint(0, 10, (3, 2, 3))

print("Dataset:")
print(data)

# average per block
print("Mean per block:")
print(data.mean(axis=1))

# flatten concept (important later)
print("Flattened idea:")
print(data.reshape(-1))