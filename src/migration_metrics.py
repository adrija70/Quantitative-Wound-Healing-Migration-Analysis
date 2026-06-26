from pathlib import Path

import pandas as pd
import numpy as np

BASE = Path(
"/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

tracks = pd.read_csv(
    BASE / "tracks_dataframe.csv"
)

MIN_TRACK_LENGTH = 10

track_sizes = (
    tracks
    .groupby("track_id")
    .size()
)

valid_tracks = track_sizes[
    track_sizes >= MIN_TRACK_LENGTH
].index

tracks = tracks[
    tracks["track_id"].isin(valid_tracks)
].copy()

print("Tracks retained:", tracks["track_id"].nunique())

results = []

for track_id, df in tracks.groupby("track_id"):

    df = df.sort_values("frame")

    dx = np.diff(df["x"])
    dy = np.diff(df["y"])

    step_lengths = np.sqrt(
        dx**2 + dy**2
    )

    path_length = step_lengths.sum()

    net_dx = (
        df["x"].iloc[-1]
        -
        df["x"].iloc[0]
    )

    net_dy = (
        df["y"].iloc[-1]
        -
        df["y"].iloc[0]
    )

    displacement = np.sqrt(
        net_dx**2 +
        net_dy**2
    )

    duration = (
        df["frame"].iloc[-1]
        -
        df["frame"].iloc[0]
    )

    mean_speed = (
        path_length /
        duration
        if duration > 0
        else np.nan
    )

    persistence = (
        displacement /
        path_length
        if path_length > 0
        else np.nan
    )

    results.append(
        {
            "track_id": track_id,
            "n_frames": len(df),
            "path_length": path_length,
            "displacement": displacement,
            "mean_speed": mean_speed,
            "persistence": persistence
        }
    )

metrics = pd.DataFrame(results)

print(metrics.head())

print("\nSummary\n")
print(
    metrics[
        [
            "path_length",
            "displacement",
            "mean_speed",
            "persistence"
        ]
    ].describe()
)

metrics.to_csv(
    BASE / "migration_metrics.csv",
    index=False
)

print("\nSaved migration_metrics.csv")
