from pathlib import Path

import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter
from skimage.filters import threshold_otsu
from skimage.morphology import (
    remove_small_objects,
    binary_closing,
    disk
)

BASE = Path(
"/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

DATA_DIR = BASE / "data"
FIG_DIR = BASE / "figures"

img = tiff.imread(
DATA_DIR / "MAX_CTRL_Wound3_project_denoised.tif"
)

# First timepoint
nuclei = img[0,1]

# Smooth
blurred = gaussian_filter(nuclei, sigma=2)

# Threshold
th = threshold_otsu(blurred)

cells = blurred > th

# Clean mask
cells = binary_closing(cells, disk(5))
cells = remove_small_objects(cells, min_size=500)

# Wound = inverse
from skimage.measure import label

wound = ~cells

labels = label(wound)

largest_region = np.argmax(
    np.bincount(labels.flat)[1:]
) + 1

wound = labels == largest_region

print("Wound area (pixels):", wound.sum())

fig, ax = plt.subplots(1,3,figsize=(18,6))

ax[0].imshow(nuclei,cmap="gray")
ax[0].set_title("Nuclei")

ax[1].imshow(cells,cmap="gray")
ax[1].set_title("Cell Region")

ax[2].imshow(wound,cmap="gray")
ax[2].set_title("Wound Mask")

for a in ax:
    a.axis("off")

plt.tight_layout()

plt.savefig(
FIG_DIR / "wound_segmentation_t0.png",
dpi=300
)

plt.show()
