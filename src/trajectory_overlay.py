from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(
"/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

tracks = pd.read_csv(
    BASE / "tracks_dataframe.csv"
)

track_lengths = (
    tracks
    .groupby("track_id")
    .size()
)

valid_tracks = track_lengths[
    track_lengths >= 20
].index

tracks = tracks[
    tracks["track_id"].isin(valid_tracks)
]

plt.figure(figsize=(8,8))

for track_id, df in tracks.groupby("track_id"):

    df = df.sort_values("frame")

    plt.plot(
        df["x"],
        df["y"],
        alpha=0.2,
        linewidth=0.5
    )

plt.gca().invert_yaxis()

plt.xlabel("X position")
plt.ylabel("Y position")

plt.title(
    "Cell Migration Trajectories"
)

plt.tight_layout()

plt.savefig(
    BASE / "figures" /
    "trajectory_overlay.png",
    dpi=300
)

plt.show()
