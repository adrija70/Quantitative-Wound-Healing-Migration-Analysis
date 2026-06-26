from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(
"/home/adrija/projects/Python-based image analysis pipelines/Wound Healing"
)

xml_file = (
BASE
/
"data"
/
"MAX_CTRL_Wound3_project_denoised_Tracks.xml"
)

tree = ET.parse(xml_file)

root = tree.getroot()

print("ROOT:")
print(root.tag)

print("\nCHILDREN:")

for child in root:
    print(child.tag)
