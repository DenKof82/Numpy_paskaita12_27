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

#del c_img
#c_img = img.copy()
