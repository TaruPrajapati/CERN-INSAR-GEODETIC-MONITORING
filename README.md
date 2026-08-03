# 🛰️ Satellite InSAR Geodetic Monitoring for CERN Underground Infrastructure

CERN InSAR Geodetic Monitoring & Structural Risk Dashboard-
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cern-insar-geodetic-monitoring-8qgkrxlzpkjvtek2dawhpu.streamlit.app)

An end-to-end spaceborne synthetic aperture radar (SAR) time-series processing pipeline and interactive geodetic deformation dashboard. This project processes multi-year Sentinel-1 C-band SAR stacks using Small BAseline Subset (SBAS) inversion via MintPy to measure millimeter-level surface deformation, mapping sub-surface structural risk for accelerator caverns and tunnel networks.

---

## 📊 Key Results & Geodetic Visualizations

### 1. Cumulative Displacement Map
![Cumulative Displacement](final_cumulative_displacement.png)

### 🔍 Map Interpretation & Analysis

* **Timeframe:** Tracks ground surface deformation from **April 09, 2024 to November 18, 2025**.
* **Color Scale (Cumulative Displacement in cm):**
  * **🔴 Red / Orange Areas (+2 to +5 cm):** Indicate surface **uplift or positive ground movement** relative to the satellite line-of-sight.
  * **🟢 Green Areas (~0 cm):** Represent **stable ground** with minimal to no detected motion.
  * **🔵 Blue Areas (-2 to -5 cm):** Indicate **subsidence or ground settlement**, pointing to potential structural risk zones near CERN underground caverns and tunnel networks.
* **Core Application:** Automatically flags high-risk geodetic anomalies to assist structural safety teams in monitoring underground infrastructure stability.

### 2. Line-of-Sight (LOS) Velocity Field
![Velocity Map](velocity_map.png)

---

## 🗂️ Core Repository Deliverables

* 💻 **`app.py`**: Streamlit interactive web application for real-time pixel time-series extraction and anomaly thresholding.
* 📓 **`Untitled.ipynb`**: Complete Python / MintPy SBAS inversion and time-series processing notebook.
* 🗺️ **`velocity.kmz`**: 3D spatial velocity map formatted for interactive inspection in Google Earth.
* 📊 **`cern_insar_anomalies.xlsx`**: Filtered geodetic risk report capturing high-subsidence pixels ($<-30\text{ mm}$).

---

## 🚀 Interactive Streamlit Dashboard Features

* **Point Time-Series Extraction:** Allows users to query exact column ($X$) and row ($Y$) coordinates to render local ground displacement trends over time.
* **Automated Anomaly Detection:** Dynamically scans the full spatial extent for pixels breaching pre-set displacement thresholds.
* **Geotechnical Report Export:** Generates structured anomaly reports (`.csv`/`.xlsx`) for structural engineering evaluation.

---

## 📊 What the Dashboard Shows
 Launch Live Interactive Dashboard : [CERN InSAR Dashboard](https://cern-insar-geodetic-monitoring-8qgkrxlzpkjvtek2dawhpu.streamlit.app/)

1. **Interactive Geodetic Deformation Heatmap:**
   * Visualizes 2D ground deformation across CERN infrastructure over time using Sentinel-1 Synthetic Aperture Radar (SAR) imagery.
   * Color-coded spatial distribution highlighting areas of subsidence (ground sinking) and uplift (ground rising).

2. **Pixel-Level Time-Series Extraction:**
   * Allows users to select specific pixel coordinates $(X, Y)$ to plot the complete motion history (2024–2025) of any target point on the ground.

3. **Dynamic Risk Thresholding & Anomaly Flagging:**
   * A configurable sidebar slider allows engineers to set subsidence risk thresholds (e.g., $-30\text{ mm}$).
   * Automatically counts and isolates high-risk pixels exceeding safety thresholds.

4. **Automated Anomaly Report Generation:**
   * Exports extracted high-risk geodetic anomalies directly into downloadable CSV format (`cern_insar_anomalies.csv`) for structural engineers.

---

## 🎯 Key Findings from Analysis

* **Identified Subsidence Hotspots:** Discovered localized ground settlement areas exhibiting ground subsidence exceeding **$-30\text{ mm}$ to $-120\text{ mm}$**, posing potential risks to structural stability above deep underground caverns.
* **Geospatial Motion Trends:** Temporal time-series plots reveal steady linear subsidence over the monitoring period (April 2024 – November 2025), rather than abrupt isolated shifts.
* **Spatial Extent:** The majority of the monitored region demonstrates stable conditions (near $0\text{ cm}$ displacement), allowing focused inspection solely on identified anomaly clusters.

---

## 💡 How This Project Solves Real-World Problems

### 🔴 The Problem:
* Underground particle physics infrastructure (like CERN’s Large Hadron Collider) relies on millimeter-level alignment across tens of kilometers of tunnels and large experimental caverns.
* Traditional ground surveys (leveling, GPS stations) are costly, labor-intensive, and only measure discrete points periodically, leaving spatial gaps between survey stations.

### 🟢 The Solution Provided by This Pipeline:
1. **Wide-Area Continuous Monitoring:** Utilizes spaceborne Sentinel-1 satellite radar data to cover hundreds of square kilometers continuously without requiring ground access.
2. **Early Warning System:** Automated anomaly detection alerts infrastructure teams to potential ground deformation before visible surface cracks or structural damage occur.
3. **Cost-Effective Inspection:** Prioritizes physical ground inspections by pinpointing exact pixel coordinates $(X, Y)$ where settlement occurs, saving time and operational resources.
