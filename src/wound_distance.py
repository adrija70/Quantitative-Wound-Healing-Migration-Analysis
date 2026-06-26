import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent

ANALYSIS_DIR = PROJECT_DIR / "analysis"
FIGURE_DIR = PROJECT_DIR / "figures"

FIGURE_DIR.mkdir(exist_ok=True)


tracks = pd.read_csv(
    ANALYSIS_DIR / "tracks_dataframe.csv"
)

metrics = pd.read_csv(
    ANALYSIS_DIR / "migration_metrics.csv"
)

print("Tracks:", len(tracks))
print("Cells:", len(metrics))

first_frame = tracks[
    tracks["frame"] == tracks["frame"].min()
]

wound_edge_x = first_frame["x"].min()

print(
    "Estimated wound edge:",
    wound_edge_x
)
mean_x = (
    tracks.groupby("track_id")["x"]
    .mean()
)

metrics["mean_x"] = metrics["track_id"].map(
    mean_x
)

metrics["distance_to_wound"] = (
    metrics["mean_x"] - wound_edge_x
)

metrics["distance_bin"] = pd.qcut(
    metrics["distance_to_wound"],
    q=4,
    labels=[
        "Nearest",
        "Near",
        "Far",
        "Farthest"
    ]
)

plt.figure(figsize=(8,6))

metrics.boxplot(
    column="mean_speed",
    by="distance_bin"
)

plt.ylabel("Mean speed")

plt.title(
    "Speed vs Distance from Wound"
)

plt.suptitle("")

plt.savefig(
    FIGURE_DIR /
    "speed_vs_distance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(8,6))

metrics.boxplot(
    column="persistence",
    by="distance_bin"
)

plt.ylabel("Persistence")

plt.title(
    "Persistence vs Distance from Wound"
)

plt.suptitle("")

plt.savefig(
    FIGURE_DIR /
    "persistence_vs_distance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(8,6))

metrics.boxplot(
    column="displacement",
    by="distance_bin"
)

plt.ylabel("Displacement")

plt.title(
    "Displacement vs Distance from Wound"
)

plt.suptitle("")

plt.savefig(
    FIGURE_DIR /
    "displacement_vs_distance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

summary = (
    metrics.groupby("distance_bin")
    [
        [
            "mean_speed",
            "persistence",
            "displacement"
        ]
    ]
    .agg(
        ["mean","std"]
    )
)

summary.to_csv(
    ANALYSIS_DIR /
    "distance_from_wound_summary.csv"
)

print(summary)

print(
    "\nSaved:"
)

print(
    "speed_vs_distance.png"
)

print(
    "persistence_vs_distance.png"
)

print(
    "displacement_vs_distance.png"
)

print(
    "distance_from_wound_summary.csv"
)
