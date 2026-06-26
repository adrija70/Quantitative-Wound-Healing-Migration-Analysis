from pathlib import Path
import xml.etree.ElementTree as ET

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

print("ROOT TAG:")
print(root.tag)

print("\nROOT ATTRIBUTES:")
print(root.attrib)

print("\nFIRST CHILD:")
print(root[0].tag)

print("\nFIRST CHILD ATTRIBUTES:")
print(root[0].attrib)
