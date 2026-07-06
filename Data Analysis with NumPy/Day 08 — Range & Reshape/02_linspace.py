import numpy as np

# =========================
# np.linspace → equal interval data তৈরি করে
# =========================

# start, end (inclusive), number of points
arr = np.linspace(0, 10, 5)

print("Linspace Array:", arr)

# বেশি smooth data generation
arr2 = np.linspace(0, 1, 10)

print("\nMore smooth data:", arr2)

# real-world example: graph plotting points
x = np.linspace(-5, 5, 100)

print("\nGraph X points:", x[:10])  # শুধু প্রথম 10 দেখাচ্ছি