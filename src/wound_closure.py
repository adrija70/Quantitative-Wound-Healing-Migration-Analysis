from pathlib import Path

import tifffile as tiff
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter

from skimage.filters import threshold_otsu
from skimage.measure import label
from skimage.morphology import (
    binary_closing,
    remove_small_objects,
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

areas = []

for t in range(img.shape[0]):

    nuclei = img[t,1]

    blurred = gaussian_filter(
        nuclei,
        sigma=2
    )

    thresh = threshold_otsu(
        blurred
    )

    cells = blurred > thresh

    cells = binary_closing(
        cells,
        disk(5)
    )

    cells = remove_small_objects(
        cells,
        min_size=500
    )

    wound = ~cells

    labels = label(wound)

    largest_region = (
        np.argmax(
            np.bincount(
                labels.flat
            )[1:]
        ) + 1
    )

    wound = labels == largest_region

    area = wound.sum()

    areas.append(area)

df = pd.DataFrame(
    {
        "frame": np.arange(len(areas)),
        "wound_area": areas
    }
)

df["normalized_area"] = (
    df["wound_area"]
    /
    df["wound_area"].iloc[0]
)

print(df.head())

df.to_csv(
    BASE / "results_wound_area.csv",
    index=False
)

plt.figure(figsize=(8,5))

plt.plot(
    df["frame"],
    df["normalized_area"],
    linewidth=3
)

plt.xlabel("Frame")
plt.ylabel("Normalized wound area")
plt.title("Wound Closure Kinetics")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "wound_closure_curve.png",
    dpi=300
)

plt.show()
