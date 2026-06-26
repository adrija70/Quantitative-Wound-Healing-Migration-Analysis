from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


BASE = Path(
    "/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

FIG_DIR = BASE / "figures"
FIG_DIR.mkdir(exist_ok=True)

tracks = pd.read_csv(
    BASE / "tracks_dataframe.csv"
)

metrics = pd.read_csv(
    BASE / "migration_metrics.csv"
)

print("Tracks dataframe:", tracks.shape)
print("Metrics dataframe:", metrics.shape)


MIN_TRACK_LENGTH = 10

track_lengths = (
    tracks
    .groupby("track_id")
    .size()
)

valid_tracks = track_lengths[
    track_lengths >= MIN_TRACK_LENGTH
].index

tracks = tracks[
    tracks["track_id"].isin(valid_tracks)
].copy()

metrics = metrics[
    metrics["track_id"].isin(valid_tracks)
].copy()

print(
    "Retained tracks:",
    tracks["track_id"].nunique()
)


trajectory_summary = []

for track_id, df in tracks.groupby("track_id"):

    df = df.sort_values("frame")

    x0 = df["x"].iloc[0]
    y0 = df["y"].iloc[0]

    x1 = df["x"].iloc[-1]
    y1 = df["y"].iloc[-1]

    dx = x1 - x0
    dy = y1 - y0

    displacement = np.sqrt(
        dx**2 + dy**2
    )

    angle = np.arctan2(
        dy,
        dx
    )

    trajectory_summary.append(
        {
            "track_id": track_id,
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "dx": dx,
            "dy": dy,
            "displacement": displacement,
            "angle": angle
        }
    )

trajectory_summary = pd.DataFrame(
    trajectory_summary
)


plt.figure(figsize=(8,5))

plt.hist(
    np.degrees(
        trajectory_summary["angle"]
    ),
    bins=36
)

plt.xlabel("Migration angle (degrees)")
plt.ylabel("Cell count")
plt.title("Migration Directionality")

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "directionality_histogram.png",
    dpi=300
)

plt.close()

angles = trajectory_summary[
    "angle"
].values

fig = plt.figure(
    figsize=(7,7)
)

ax = fig.add_subplot(
    111,
    projection="polar"
)

ax.hist(
    angles,
    bins=24
)

ax.set_title(
    "Migration Rose Plot"
)

plt.savefig(
    FIG_DIR /
    "rose_plot.png",
    dpi=300
)

plt.close()


max_lag = 20

msd_values = []

for lag in range(
    1,
    max_lag + 1
):

    lag_displacements = []

    for track_id, df in tracks.groupby(
        "track_id"
    ):

        df = df.sort_values(
            "frame"
        )

        coords = df[
            ["x","y"]
        ].values

        if len(coords) <= lag:
            continue

        diffs = (
            coords[lag:]
            -
            coords[:-lag]
        )

        sqdist = (
            diffs[:,0]**2
            +
            diffs[:,1]**2
        )

        lag_displacements.extend(
            sqdist
        )

    msd_values.append(
        np.mean(
            lag_displacements
        )
    )

msd_df = pd.DataFrame(
    {
        "lag": np.arange(
            1,
            max_lag + 1
        ),
        "MSD": msd_values
    }
)

plt.figure(figsize=(7,5))

plt.plot(
    msd_df["lag"],
    msd_df["MSD"],
    marker="o"
)

plt.xlabel("Lag")
plt.ylabel("MSD")

plt.title(
    "Mean Squared Displacement"
)

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "msd_curve.png",
    dpi=300
)

plt.close()

plt.figure(figsize=(7,5))

plt.loglog(
    msd_df["lag"],
    msd_df["MSD"],
    marker="o"
)

plt.xlabel("Lag")
plt.ylabel("MSD")

plt.title(
    "MSD (Log-Log)"
)

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "msd_loglog.png",
    dpi=300
)

plt.close()

plt.figure(figsize=(8,8))

plt.hist2d(
    tracks["x"],
    tracks["y"],
    bins=75
)

plt.colorbar(
    label="Cell density"
)

plt.gca().invert_yaxis()

plt.title(
    "Cell Density Map"
)

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "density_heatmap.png",
    dpi=300
)

plt.close()

vx = []
vy = []
px = []
py = []

for track_id, df in tracks.groupby(
    "track_id"
):

    df = df.sort_values(
        "frame"
    )

    x = df["x"].values
    y = df["y"].values

    if len(x) < 2:
        continue

    px.extend(
        x[:-1]
    )

    py.extend(
        y[:-1]
    )

    vx.extend(
        np.diff(x)
    )

    vy.extend(
        np.diff(y)
    )

step = 50

plt.figure(figsize=(8,8))

plt.quiver(
    px[::step],
    py[::step],
    vx[::step],
    vy[::step]
)

plt.gca().invert_yaxis()

plt.title(
    "Velocity Field"
)

plt.tight_layout()

plt.savefig(
    FIG_DIR /
    "velocity_field.png",
    dpi=300
)

plt.close()


summary = pd.DataFrame(
    {
        "metric":[
            "n_tracks",
            "mean_speed",
            "mean_persistence",
            "mean_displacement"
        ],
        "value":[
            metrics["track_id"].nunique(),
            metrics["mean_speed"].mean(),
            metrics["persistence"].mean(),
            metrics["displacement"].mean()
        ]
    }
)

summary.to_csv(
    BASE /
    "advanced_migration_summary.csv",
    index=False
)

print(
    "\nAnalysis complete."
)

print(
    "Figures saved to:",
    FIG_DIR
)
