# src/advanced_analysis.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANALYSIS_DIR = os.path.join(BASE_DIR, "analysis")
OUTPUT_DIR = os.path.join(ANALYSIS_DIR, "advanced_outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


tracks = pd.read_csv(
    os.path.join(ANALYSIS_DIR, "tracks_dataframe.csv")
)

metrics = pd.read_csv(
    os.path.join(ANALYSIS_DIR, "migration_metrics.csv")
)

print("Tracks:", len(tracks))
print("Cells:", metrics.shape[0])


# FIGURE 10
# DISTANCE FROM WOUND SURROGATE
print("Running Figure 10...")

mean_x = tracks.groupby("track_id")["x"].mean()

metrics["mean_x"] = metrics["track_id"].map(mean_x)

front_threshold = np.percentile(
    metrics["mean_x"],
    25
)

rear_threshold = np.percentile(
    metrics["mean_x"],
    75
)

conditions = [
    metrics["mean_x"] <= front_threshold,
    metrics["mean_x"] >= rear_threshold
]

choices = [
    "front",
    "rear"
]

metrics["region"] = np.select(
    conditions,
    choices,
    default="middle"
)

plt.figure(figsize=(8,6))

for region in ["front","middle","rear"]:

    vals = metrics.loc[
        metrics["region"] == region,
        "mean_speed"
    ]

    plt.boxplot(
        vals,
        positions=[["front","middle","rear"].index(region)]
    )

plt.xticks(
    [0,1,2],
    ["Front","Middle","Rear"]
)

plt.ylabel("Mean speed")
plt.title("Speed by Position")

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "speed_front_middle_rear.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# FIGURE 11
# WOUND FRONT KYMOGRAPH SURROGATE

print("Running Figure 11...")

front_position = (
    tracks.groupby("frame")["x"]
    .min()
)

plt.figure(figsize=(8,5))

plt.plot(
    front_position.index,
    front_position.values,
    linewidth=3
)

plt.xlabel("Frame")
plt.ylabel("Leading edge position")

plt.title("Wound Front Progression")

plt.grid(True)

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "wound_front_progression.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# FIGURE 12
# CONTOUR EVOLUTION SURROGATE
print("Running Figure 12...")

selected_frames = [0,16,32,48,63]

plt.figure(figsize=(8,6))

for frame in selected_frames:

    subset = tracks[
        tracks["frame"] == frame
    ]

    plt.scatter(
        subset["x"],
        subset["y"],
        s=5,
        alpha=0.4,
        label=f"T={frame}"
    )

plt.gca().invert_yaxis()

plt.legend()

plt.title(
    "Cell Front Evolution"
)

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "front_evolution.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# FIGURE 13
# SPEED MAP


print("Running Figure 13...")

plt.figure(figsize=(8,8))

plt.hexbin(
    metrics["mean_x"],
    metrics["displacement"],
    C=metrics["mean_speed"],
    gridsize=30,
    reduce_C_function=np.mean
)

plt.colorbar(
    label="Mean speed"
)

plt.xlabel("Mean X")
plt.ylabel("Displacement")

plt.title(
    "Migration Speed Landscape"
)

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "speed_heatmap.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# FIGURE 14
# COLLECTIVE ORDER PARAMETER

print("Running Figure 14...")

angles = []

for track_id, group in tracks.groupby("track_id"):

    group = group.sort_values("frame")

    dx = group["x"].iloc[-1] - group["x"].iloc[0]
    dy = group["y"].iloc[-1] - group["y"].iloc[0]

    theta = np.arctan2(
        dy,
        dx
    )

    angles.append(theta)

angles = np.array(angles)

order_parameter = np.abs(
    np.mean(
        np.exp(1j*angles)
    )
)

with open(
    os.path.join(
        OUTPUT_DIR,
        "collective_order_parameter.txt"
    ),
    "w"
) as f:

    f.write(
        f"Order parameter = {order_parameter:.4f}\n"
    )

print(
    "Order parameter:",
    order_parameter
)

# FIGURE 15
# FRONT VS REAR COMPARISON

print("Running Figure 15...")

fig, ax = plt.subplots(
    1,
    3,
    figsize=(15,5)
)

for i, metric_name in enumerate([
    "mean_speed",
    "displacement",
    "persistence"
]):

    front = metrics.loc[
        metrics["region"]=="front",
        metric_name
    ]

    rear = metrics.loc[
        metrics["region"]=="rear",
        metric_name
    ]

    ax[i].boxplot(
        [front,rear],
        tick_labels=["Front","Rear"]
    )

    ax[i].set_title(
        metric_name
    )

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "front_vs_rear_comparison.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Finished.")
print("Results saved to:")
print(OUTPUT_DIR)
