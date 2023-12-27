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