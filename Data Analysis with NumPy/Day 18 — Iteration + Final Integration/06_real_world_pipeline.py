import numpy as np

# -----------------------------------
# FULL DATA ANALYSIS PIPELINE
# -----------------------------------

# Step 1: Generate data (simulate marks)
data = np.random.randint(0, 100, 20)

print("Data:", data)

# Step 2: Clean/filter
clean = data[data >= 40]

print("Clean Data:", clean)

# Step 3: Normalize (basic scaling)
normalized = clean / 100

print("Normalized:", normalized)

# Step 4: Statistics
print("Mean:", np.mean(clean))
print("Max:", np.max(clean))
print("Min:", np.min(clean))

# Step 5: Insight
print("\nINSIGHT:")
print("Total:", len(data))
print("Valid:", len(clean))
print("Failure Rate:", (len(data) - len(clean)) / len(data))