from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

BASE = Path(
"/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

xml_file = (
BASE /
"data" /
"MAX_CTRL_Wound3_project_denoised_Tracks.xml"
)

tree = ET.parse(xml_file)
root = tree.getroot()

rows = []

for track_id, particle in enumerate(root):

    for detection in particle:

        rows.append(
            {
                "track_id": track_id,
                "frame": int(detection.attrib["t"]),
                "x": float(detection.attrib["x"]),
                "y": float(detection.attrib["y"]),
                "z": float(detection.attrib["z"])
            }
        )

tracks = pd.DataFrame(rows)

print("\nTracks dataframe")
print(tracks.head())

print("\nShape")
print(tracks.shape)

print("\nUnique tracks")
print(tracks["track_id"].nunique())

tracks.to_csv(
    BASE / "tracks_dataframe.csv",
    index=False
)

print("\nSaved tracks_dataframe.csv")
