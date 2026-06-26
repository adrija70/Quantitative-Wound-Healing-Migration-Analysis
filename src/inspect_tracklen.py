from pathlib import Path
import pandas as pd

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

print(track_lengths.describe())
