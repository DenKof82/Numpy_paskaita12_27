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
plt.axis("off")
#plt.show()
img = image_np
print(img.shape)
c_img = img.copy()
c_img[:,:,0] = np.clip(c_img[:,:,0].astype('int16') + 50, 0, 255).astype('uint8')
plt.imshow(c_img)
plt.axis("off")
#plt.show()
del c_img
c_img = img.copy()

palette = ["CE1483","CE1483","CE1483","CE1483","CE1483"]

def hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
  return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

palette = [hex_to_rgb(h) for h in palette]
print(palette)


def find_nearest_palatte_color(pixel: np.array, palette: list[tuple[int, int, int]]) -> tuple[int, int, int]:
  # Calculate the Euclidean distance between the pixel and each color in the palette
  distances = np.sqrt(np.sum((palette - pixel) ** 2, axis=1))
  # find the index of the nearest color
  nearest_color_index = np.argmin(distances)
  return palette[nearest_color_index]


find_nearest_palatte_color(np.array([70, 30, 20]), palette)

plt.imshow(c_img)
plt.axis("off")
plt.show()