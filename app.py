import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from shapely.geometry import Point

st.set_page_config(layout="wide", page_title="CERN InSAR Geodetic Dashboard")

st.title("🛰️ Geodetic Deformation & Structural Risk Dashboard")
st.markdown("### Automated InSAR Monitoring Pipeline for CERN Infrastructure")

# File path
FILE_PATH = 'timeseries.h5'

@st.cache_data
def load_data():
    if not os.path.exists(FILE_PATH):
        return None, None, None

    with h5py.File(FILE_PATH, 'r') as f:
        # Convert displacement to mm
        ts_data = f['timeseries'][:] * 1000
        dates = [d.decode('utf-8') for d in f['date'][:]]
        dates_dt = pd.to_datetime(dates, format='%Y%m%d')
        cum_disp = ts_data[-1, :, :]  # Final cumulative displacement slice
        return ts_data, dates_dt, cum_disp

ts_data, dates_dt, cum_disp = load_data()

# Sidebar - Anomaly Threshold Configuration
st.sidebar.header("⚠️ Risk Threshold Settings")
subsidence_threshold = st.sidebar.slider(
    "Flag Subsidence Threshold (mm)",
    min_value=-100, max_value=0, value=-30, step=5
)

# Mode check: Full HDF5 data vs Extracted Anomaly fallback
if ts_data is not None:
    # Anomaly Detection Logic
    rows, cols = cum_disp.shape
    y_indices, x_indices = np.where(cum_disp < subsidence_threshold)
    anomaly_count = len(x_indices)

    st.sidebar.metric(label="Detected Anomaly Pixels", value=anomaly_count)

    # Save Anomaly Report as CSV
    if anomaly_count > 0:
        anomaly_df = pd.DataFrame({
            'Row_Y': y_indices,
            'Col_X': x_indices,
            'Cumulative_Disp_mm': cum_disp[y_indices, x_indices]
        })

        st.sidebar.download_button(
            label="📥 Download Anomaly Report (CSV)",
            data=anomaly_df.to_csv(index=False).encode('utf-8'),
            file_name='cern_insar_anomalies.csv',
            mime='text/csv',
        )

    # Dashboard Layout: 2 Columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Cumulative Displacement Heatmap")
        fig, ax = plt.subplots(figsize=(6, 5))
        im = ax.imshow(cum_disp, cmap='jet_r', vmin=-50, vmax=50)
        plt.colorbar(im, ax=ax, label="Displacement (mm)")
        ax.set_title("Click Target Coordinates Below")
        st.pyplot(fig)

    with col2:
        st.subheader("Pixel Time-Series Extraction")

        # Coordinate Selectors
        selected_col = st.number_input("Column (X)", min_value=0, max_value=cols-1, value=cols//2)
        selected_row = st.number_input("Row (Y)", min_value=0, max_value=rows-1, value=rows//2)

        pixel_ts = ts_data[:, selected_row, selected_col]

        fig_ts, ax_ts = plt.subplots(figsize=(7, 4))
        ax_ts.plot(dates_dt, pixel_ts, 'o-', color='#d62728', linewidth=2, markersize=4)
        ax_ts.axhline(0, color='black', linestyle='--', alpha=0.5)
        ax_ts.set_title(f"Displacement History for Pixel ({selected_col}, {selected_row})")
        ax_ts.set_xlabel("Date")
        ax_ts.set_ylabel("Displacement (mm)")
        ax_ts.grid(True, linestyle=':', alpha=0.6)
        plt.xticks(rotation=45)
        st.pyplot(fig_ts)

else:
    # Online Fallback View when timeseries.h5 is not on cloud
    st.warning("⚠️ Full 1 GB+ 'timeseries.h5' dataset is stored locally.")
    st.info("Displaying extracted CERN InSAR structural anomaly dataset for online review.")
    
    if os.path.exists('cern_insar_anomalies.xlsx'):
        df = pd.read_excel('cern_insar_anomalies.xlsx')
        st.subheader("📊 Extracted High-Risk Geodetic Anomaly Table")
        st.dataframe(df, use_container_width='stretch')
    else:
        st.error("No data files found in repository.")
