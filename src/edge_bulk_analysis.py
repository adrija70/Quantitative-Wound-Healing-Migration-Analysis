from pathlib import Path

import numpy as np
import pandas as pd
import tifffile as tiff

from scipy.ndimage import (
    gaussian_filter,
    distance_transform_edt
)

from skimage.filters import threshold_otsu
from skimage.measure import label
from skimage.morphology import (
    disk,
    binary_closing,
    remove_small_objects
)

BASE = Path(
    "/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

IMG_FILE = BASE / "data" / "MAX_CTRL_Wound3_project_denoised.tif"

TRACKS_FILE = BASE / "tracks_dataframe.csv"

FIG_DIR = BASE / "figures"
FIG_DIR.mkdir(exist_ok=True)


img = tiff.imread(IMG_FILE)

print("Image shape:", img.shape)

# T,C,Y,X
nuclei = img[0, 1]


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
        np.bincount(labels.flat)[1:]
    )
    + 1
)

wound = labels == largest_region

print(
    "Wound area:",
    wound.sum()
)


distance_map = distance_transform_edt(
    ~wound
)


tracks = pd.read_csv(
    TRACKS_FILE
)

print(
    "Tracks:",
    len(tracks)
)


first_pos = (
    tracks
    .sort_values("frame")
    .groupby("track_id")
    .first()
    .reset_index()
)


distances = []

for _, row in first_pos.iterrows():

    x = int(round(row["x"]))
    y = int(round(row["y"]))

    if (
        x < 0
        or x >= distance_map.shape[1]
        or y < 0
        or y >= distance_map.shape[0]
    ):
        continue

    distances.append(
        {
            "track_id": row["track_id"],
            "distance_to_wound": distance_map[y, x]
        }
    )

distance_df = pd.DataFrame(
    distances
)

print(
    "Cells assigned:",
    len(distance_df)
)


metrics = pd.read_csv(
    BASE / "migration_metrics.csv"
)


metrics = metrics.merge(
    distance_df,
    on="track_id"
)


EDGE_DISTANCE = 100

metrics["group"] = np.where(
    metrics["distance_to_wound"] <= EDGE_DISTANCE,
    "edge",
    "bulk"
)

print("\nGroup counts\n")

print(
    metrics["group"].value_counts()
)

print("\nSummary\n")

summary = (
    metrics
    .groupby("group")[
        [
            "mean_speed",
            "persistence",
            "displacement"
        ]
    ]
    .agg(
        ["mean", "std"]
    )
)

print(summary)

summary.to_csv(
    BASE / "edge_bulk_summary.csv"
)

metrics.to_csv(
    BASE / "edge_bulk_metrics.csv",
    index=False
)

print(
    "\nSaved edge_bulk_summary.csv"
)

print(
    "Saved edge_bulk_metrics.csv"
)
