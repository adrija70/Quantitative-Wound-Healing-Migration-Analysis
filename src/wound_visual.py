import tifffile as tiff
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path("/home/adrija/projects/Python-based image analysis pipelines/Wound Healing")
img_path = BASE / "data" / "MAX_CTRL_Wound3_project_denoised.tif"
fig_dir  = BASE / "figures"

assert img_path.exists(), f"input not found: {img_path}"
fig_dir.mkdir(parents=True, exist_ok=True)

img = tiff.imread(img_path)
print("loaded", img.shape, img.dtype)
assert img.ndim == 4 and img.shape[1] >= 2, f"expected (T,C,Y,X) with >=2 channels, got {img.shape}"

frames = [0, 16, 32, 48, 63]
assert max(frames) < img.shape[0], f"only {img.shape[0]} timepoints, cannot index {max(frames)}"

fig, ax = plt.subplots(2, 5, figsize=(18, 8))
for i, f in enumerate(frames):
    ax[0, i].imshow(img[f, 0], cmap="gray"); ax[0, i].set_title(f"Membrane T={f}"); ax[0, i].axis("off")
    ax[1, i].imshow(img[f, 1], cmap="gray"); ax[1, i].set_title(f"Nuclei T={f}");   ax[1, i].axis("off")
plt.tight_layout()
plt.savefig(fig_dir / "dataset_overview.png", dpi=300)
plt.show()
