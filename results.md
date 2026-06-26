## Results

### Wound Segmentation Enables Quantitative Measurement of Healing Dynamics

Automated image segmentation was used to identify the wound region throughout the timelapse sequence. Binary wound masks accurately separated cell-covered and cell-free regions, enabling objective measurement of wound area and front position over time.

![Wound Segmentation](figures/wound_segmentation_t0.png)

![Wound Mask Analysis](figures/Figure_2.png)

---

### Progressive Wound Closure Observed During Collective Migration

Quantification of wound area demonstrated continuous reduction of the open wound region throughout the experiment. Closure kinetics revealed coordinated migration of the epithelial sheet toward the wound center, resulting in gradual restoration of monolayer continuity.

![Wound Closure Curve](figures/wound_closure_curve.png)

---

### Wound Front Advancement Reveals Coordinated Tissue Movement

Tracking of the leading edge showed progressive advancement of the wound front. Regression-based estimation of front position demonstrated approximately monotonic closure behavior with minimal evidence of retraction events.

![Wound Front Progression](figures/wound_front_progression.png)

![Front Evolution](figures/front_evolution.png)

---

### Cell Trajectories Exhibit Directed Migration Toward the Wound

Single-cell trajectory reconstruction revealed preferential movement toward the wound region. Trajectory overlays showed coordinated directional migration rather than random motility, indicating collective guidance cues during healing.

![Trajectory Overlay](figures/trajectory_overlay.png)

![Velocity Field](figures/velocity_field.png)

---

### Migration Speed Varies Across the Tissue

Spatial analysis demonstrated differences in migration behavior depending on distance from the wound edge. Cells located near the wound front generally exhibited greater motility than cells located deeper within the monolayer.

![Speed vs Distance](figures/speed_vs_distance.png)

![Speed Front Middle Rear](figures/speed_front_middle_rear.png)

---

### Directionality and Persistence Increase Near the Wound Edge

Migration directionality analysis revealed a strong bias toward wound closure. Cells near the leading edge exhibited greater persistence and more aligned trajectories compared with cells located farther from the wound.

![Directionality Histogram](figures/directionality_histogram.png)

![Rose Plot](figures/rose_plot.png)

![Persistence vs Distance](figures/persistence_vs_distance.png)

---

### Mean Squared Displacement Indicates Sustained Directed Motion

Mean squared displacement (MSD) analysis demonstrated increasing displacement over time, consistent with active migration rather than stationary behavior. Log-log representation suggested persistent motion during wound closure.

![MSD Curve](figures/msd_curve.png)

![MSD Log-Log](figures/msd_loglog.png)

---

### Collective Migration Generates Spatially Organized Velocity Patterns

Velocity field reconstruction revealed coordinated movement across large portions of the monolayer. Cells displayed non-random collective motion directed toward the wound, producing organized flow fields that contributed to efficient closure.

![Velocity Field](figures/velocity_field.png)

![Speed Heatmap](figures/speed_heatmap.png)

![Density Heatmap](figures/density_heatmap.png)

---

### Edge Cells Display Distinct Migration Phenotypes

Comparison of cells at the wound edge versus cells in the bulk monolayer revealed significant behavioral differences. Edge cells showed enhanced speed, persistence, and directed migration, supporting their role as primary drivers of wound closure.

![Front vs Rear Comparison](figures/front_vs_rear_comparison.png)

![Displacement vs Distance](figures/displacement_vs_distance.png)

![Speed Front Middle Rear](figures/speed_front_middle_rear.png)

---
