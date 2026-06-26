# Quantitative Wound Healing Migration Analysis

A Python-based image analysis pipeline for quantifying epithelial wound closure, collective cell migration, and spatially resolved migration dynamics from time-lapse microscopy data.

---

## Dataset

### Data Source

**Dataset:** Segmentation and Tracking of Wound Healing Assays in Epithelial Cells Using Artificial Intelligence

**Link:** https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD1377

The dataset contains time-lapse fluorescence microscopy images of epithelial cell monolayers undergoing wound-healing migration following the creation of a cell-free gap. The image sequences were generated to evaluate automated segmentation and tracking approaches for quantifying collective cell migration during tissue repair.

The dataset consists of:

- Multi-frame time-lapse microscopy image sequences
- Fluorescence and phase-contrast wound-healing assays
- Epithelial cell monolayers migrating into an initially cell-free wound region
- Ground-truth annotations and tracking information for algorithm validation
- Single-cell and collective migration behaviors captured throughout wound closure

---
```mermaid
flowchart TD

A[Raw Timelapse Microscopy]
--> B[Image Inspection & Visualization]
--> C[Wound Segmentation]
--> D[Wound Closure Quantification]
--> E[Cell Tracking Import]
--> F[Single Cell Trajectories]
--> G[Spatial Migration Analysis]
--> H[Collective Migration Analysis]
--> I[Edge vs Bulk Comparison]
--> J[Wound Healing Phenotype]
```
---
## Installation
Install [anaconda](https://www.anaconda.com/) or [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).

Create a conda environment:

```bash
conda create -n qtlm python=3.11
conda activate qtlm
```

Install dependencies:

```bash
pip install -r requirements.txt
```


Please save the dataset folder in `./` as `Data` folder before starting the experiments.

---
### Wound segmentation and closure quantification

```bash
python src/wound_visual.py
python src/wound_segmentation.py
python src/wound_closure.py
```
---

### Cell trajectory reconstruction from TrackMate outputs

```bash
python src/inspect_xml.py
python src/inspect_xml2.py
python src/inspect_xml3.py
python src/parse_trackmate.py
python src/inspect_tracklen.py
```

---

### Migration speed and persistence analysis

```bash
python src/migration_metrics.py
python src/advanced_migration.py
```

---

### Spatial analysis relative to wound position

```bash
python src/wound_distance.py
python src/edge_bulk_analysis.py
```
---

### Collective migration characterization

```bash
python src/trajectory_overlay.py
python src/advanced_analysis.py
```
---

### Velocity field and directional migration analysis

```bash
python src/advanced_analysis.py
python src/advanced_migration.py
python src/trajectory_overlay.py
```
---

## Results

### Wound Segmentation Enables Quantitative Measurement of Healing Dynamics

![Wound Segmentation](figures/wound_segmentation_t0.png)

![Wound Mask Analysis](figures/Figure_2.png)

---

### Progressive Wound Closure Observed During Collective Migration

![Wound Closure Curve](figures/wound_closure_curve.png)

---

### Wound Front Advancement Reveals Coordinated Tissue Movement

![Wound Front Progression](figures/wound_front_progression.png)

![Front Evolution](figures/front_evolution.png)

---

### Cell Trajectories Exhibit Directed Migration Toward the Wound

![Trajectory Overlay](figures/trajectory_overlay.png)

![Velocity Field](figures/velocity_field.png)

---

### Migration Speed Varies Across the Tissue

![Speed vs Distance](figures/speed_vs_distance.png)

![Speed Front Middle Rear](figures/speed_front_middle_rear.png)

---

### Directionality and Persistence Increase Near the Wound Edge

![Directionality Histogram](figures/directionality_histogram.png)

![Rose Plot](figures/rose_plot.png)

![Persistence vs Distance](figures/persistence_vs_distance.png)

---

### Mean Squared Displacement Indicates Sustained Directed Motion

![MSD Curve](figures/msd_curve.png)

![MSD Log-Log](figures/msd_loglog.png)

---

### Collective Migration Generates Spatially Organized Velocity Patterns

![Velocity Field](figures/velocity_field.png)

![Speed Heatmap](figures/speed_heatmap.png)

![Density Heatmap](figures/density_heatmap.png)

---

### Edge Cells Display Distinct Migration Phenotypes

![Front vs Rear Comparison](figures/front_vs_rear_comparison.png)

![Displacement vs Distance](figures/displacement_vs_distance.png)

![Speed Front Middle Rear](figures/speed_front_middle_rear.png)

---
