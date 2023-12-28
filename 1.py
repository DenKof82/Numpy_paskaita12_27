import numpy as np
from requests import get
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

response = get("https://img.freepik.com/premium-photo/beautiful-cat-photo-beautiful-cat-cute-cat-cat-picpet_860112-7.jpg?w=360")
print(response)

image = Image.open(BytesIO(response.content))
image_np = np.array(image)
plt.imshow(image_np)
plt.axis("on")
#plt.show()
img = image_np
print(img.shape)
print(img.dtype)
c_img = img.copy()
print(img[0, 0])
#c_img[:,:,0] = np.clip(c_img[:,:,0].astype('int16') +50, 0, 255).astype('unit8')
c_img[:,:,0] = np.clip(c_img[:,:,0].astype('int16') + 50, 0, 255).astype('uint8')
print(c_img[0, 0])
plt.imshow(c_img)
plt.axis("off")
#plt.show()
del c_img
c_img = img.copy()

palette = ["F5F1ED","065143","E0A890","065143","CE1483"]

def hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
  return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

palette = [hex_to_rgb(h) for h in palette]
print(palette)

def find_nearest_palatte_color(pixel: np.array, palette: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    # Calculate the Euclidean distance between the pixel and each color in the palette
    distances = np.sqrt(np.sum((palette - pixel)**2, axis=1))
    # find the index of the nearest color
    nearest_color_index = np.argmin(distances)
    return palette[nearest_color_index]

print(find_nearest_palatte_color(np.array([70, 30, 20]), palette))

def apply_palette(image: np.array, palette: list[tuple[int, int, int]]) -> np.array:
    # Prepare an empty array for the converted image
    converted_image = np.zeros_like(image)
    # Iterate over each pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            converted_image[i, j] = find_nearest_palatte_color(image[i, j], palette)
    return converted_image

c_img = apply_palette(c_img, palette)
print(c_img[0, 0])

plt.imshow(c_img)
plt.axis("off")
plt.show()

palettes = [
    ["51cb20","76b041","639a88","3a5683","2708a0"],
    ["e6c79c","cddfa0","6fd08c","7b9ea8","78586f"],
    ["151515","a63d40","e9b872","90a959","6494aa"],
    ["c4a69d","98a886","465c69","363457","735290"],
  ]

palettes = [[hex_to_rgb(h) for h in palette] for palette in palettes]

# Visualizing palettes for easier interpretability
import matplotlib.patches as patches

fig, axs = plt.subplots(len(palettes), 1, figsize=(5, len(palettes) * 2))

for i, palette in enumerate(palettes):
  for j, colors in enumerate(palette):
    normalized = tuple(c / 255 for c in colors)
    rect = patches.Rectangle((j, 0), 1, 1, linewidth=1, edgecolor='none', facecolor=normalized)
    axs[i].add_patch(rect)

  axs[i].set_title(f"Palette {i}")
  axs[i].set_xlim(0, len(palette))
  axs[i].axis('off')

plt.tight_layout()
plt.show()

del c_img
c_img = img.copy()

# Only showing the numpy way as it is way more efficient
# And we're learning how to use numpy

# In practice remember that you can make the code simpler
# and more readable if you don't need performance

# (num_palettes x num_colors x 3)
palettes = np.array(palettes, dtype=np.int32)
# (height x width x 3)
image = c_img.astype(np.int32)

# reshape for broadcasting: (height x width x 1 x 1 x 3)
image_reshaped = image.reshape(image.shape[0], image.shape[1], 1, 1, 3)
# reshape for broadcasting: (1 x 1 x num_palettes x num_colors x 3)
palettes_reshaped = palettes.reshape(1, 1, len(palettes), -1, 3)

# calculate euclidian distances
distances = np.sqrt(np.sum((image_reshaped - palettes_reshaped) ** 2, axis=4))
distances.shape

# find minimum distance for each palette
min_dist_per_palette = np.min(distances, axis=3)
min_dist_per_palette.shape

average_distances = np.mean(min_dist_per_palette, axis=(0, 1))
average_distances

best_palette_index = np.argmin(average_distances)
best_palette = palettes[best_palette_index]
best_palette

fig, ax = plt.subplots(1, 1, figsize=(5, 1))

for j, colors in enumerate(best_palette):
    normalized = tuple(color/255 for color in colors)
    rect = patches.Rectangle((j, 0), 1, 1, linewidth=1, edgecolor='none', facecolor=normalized)
    ax.add_patch(rect)

ax.set_title(f"Palette {best_palette_index}")
ax.set_xlim(0, len(palette))
ax.axis('off')

plt.tight_layout()
plt.show()

# Image colored with palette 2
# clearing the old image, and creating a deep copy for a new one
del c_img
c_img = img.copy()

# convert image and palette to numpy arrays
palette = best_palette.copy()
c_img = c_img.astype(np.int64)

# reshape the image and palette
image_reshaped = c_img.reshape(-1, 1, 3)
palette_reshaped = palette.reshape(1, -1, 3)

distances = np.sqrt(np.sum((image_reshaped - palette_reshaped) ** 2, axis=2))
nearest_color_indices = np.argmin(distances, axis=1)
c_img = palette[nearest_color_indices].reshape(c_img.shape)

plt.imshow(c_img)
plt.axis("off")
plt.show()




