import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Modul Dimensi Tiga SMA", 
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DESAIN TAMPILAN CUSTOM (CSS) ---
style_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    .stApp p, .stApp li, .stApp span, .stApp label {
        color: #212529 !important;
    }
    h1 {
        color: #0d6efd !important;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    h2, h3 {
        color: #495057 !important;
        font-family: 'Segoe UI', sans-serif;
    }
    .sma-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 6px solid #0d6efd;
        margin-bottom: 20px;
    }
    .sma-card-tech {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 6px solid #198754;
        margin-bottom: 20px;
    }
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
sidebar_html = """
<div style='text-align: center;'>
    <h2 style='margin-bottom: 0;'>📐 Lab Dimensi Tiga</h2>
    <p style='color: #6c757d; font-size: 14px;'>Media Pembelajaran Geometri SMA</p>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

menu = st.sidebar.selectbox("", ["🏠 Beranda Analisis", "🧊 Analisis Kubus", "🧱 Analisis Balok"])

# --- FUNGSI UNTUK MEMBUAT KERANGKA STRUKTUR (WIREFRAME) ---
def get_wireframe_data(x, y, z):
    lines_idx = [
        0,1, 1,2, 2,3, 3,0, # Alas ABCD
        4,5, 5,6, 6,7, 7,4, # Tutup EFGH
        0,4, 1,5, 2,6, 3,7  # Tiang tegak AE, BF, CG, DH
    ]
    x_lines, y_lines, z_lines = [], [], []
    for i in range(0, len(lines_idx), 2):
        p1, p2 = lines_idx[i], lines_idx[i+1]
        x_lines.extend([x[p1], x[p2], None])
        y_lines.extend([y[p1], y[p2], None])
        z_lines.extend([z[p1], z[p2], None])
    return x_lines, y_lines, z_lines

# --- HALAMAN UTAMA: BERANDA ---
if menu == "🏠 Beranda Analisis":
    col_text, col_img = st.columns([3, 2])
    
    with col_text:
        st.title("Aplikasi Analisis Spasial Dimensi Tiga 🖥️")
        st.markdown("""
        ### Selamat Datang di Modul Geometri Ruang SMA!
        Aplikasi ini dirancang sebagai alat bantu visualisasi objek 3 dimensi guna mempermudah pemahaman konsep kedudukan titik, garis, dan bidang, serta perhitungan jarak dan sudut pada materi **Dimensi Tiga**.
        
        **Fitur Utama Laboratorium Virtual:**
        * 🌐 **Visualisasi Spasial Dinamis:** Manipulasi sudut pandang objek 3D secara *real-time* untuk memperkuat kemampuan spasial (membayangkan ruang).
        * 📊 **Kalkulator Struktur Geometri:** Analisis otomatis ukuran dasar
