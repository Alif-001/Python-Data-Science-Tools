import numpy as np

# Image = 3D array in real world
# (height, width, color channels)

# Example: small fake image (2x2 pixels, RGB)
image = np.array([
    [
        [255, 0, 0],   # red pixel
        [0, 255, 0]    # green pixel
    ],
    [
        [0, 0, 255],   # blue pixel
        [255, 255, 0]  # yellow pixel
    ]
])

print("Image array:")
print(image)

print("Shape:", image.shape)

# access pixel
print("Pixel (0,1):", image[0, 1])