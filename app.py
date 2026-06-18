import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Modul Dimensi Tiga SMK", 
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
    .smk-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 6px solid #0d6efd;
        margin-bottom: 20px;
    }
    .smk-card-tech {
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
    <p style='color: #6c757d; font-size: 14px;'>Media Pembelajaran Geometri SMK</p>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

menu = st.sidebar.selectbox("", ["🏠 Beranda Analisis", "🧊 Analisis Kubus", "🧱 Analisis Balok"])

# --- FUNGSI UNTUK MEMBUAT KERANGKA STRUKTUR (WIREFRAME) ---
def get_wireframe_data(x, y, z):
    # Pola garis untuk menghubungkan titik-titik menjadi kerangka kubus/balok
    lines_idx = [
        0,1, 1,2, 2,3, 3,0, # Alas
        4,5, 5,6, 6,7, 7,4, # Tutup
        0,4, 1,5, 2,6, 3,7  # Tiang tegak
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
        ### Selamat Datang di Modul Geometri Ruang SMK!
        Aplikasi ini dirancang sebagai alat bantu visualisasi objek 3 dimensi guna mempermudah pemahaman konsep kedudukan titik, garis, dan bidang, serta perhitungan jarak dan sudut pada materi **Dimensi Tiga**.
        
        **Fitur Utama Laboratorium Virtual:**
        * 🌐 **Visualisasi Spasial Dinamis:** Manipulasi sudut pandang objek 3D secara *real-time* untuk memperkuat kemampuan spasial (membayangkan ruang).
        * 📊 **Kalkulator Struktur Geometri:** Analisis otomatis ukuran dasar, luas permukaan, volume, hingga panjang **Diagonal Bidang** dan **Diagonal Ruang**.
        * 🔍 **Representasi Garis Nyata:** Objek dilengkapi dengan visualisasi rusuk/kerangka transparan untuk mempermudah penarikan garis proyeksi matematika.
        
        *Silakan pilih menu objek di sebelah kiri untuk memulai analisis.*
        """)
        
    with col_img:
        st.write("")
        st.info("💡 **Tips Pembelajaran:** Gunakan fitur *rotate* dan *zoom* pada grafis 3D untuk melihat hubungan antar titik sudut secara lebih presisi.")

# --- HALAMAN: KUBUS ---
elif menu == "🧊 Analisis Kubus":
    st.title("🧊 Analisis Geometri Ruang: Kubus (Hexahedron)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="smk-card">
            <h3>📋 Elemen Struktur Kubus</h3>
            <ul>
                <li><b>6 Sisi (Bidang):</b> Seluruhnya berbentuk persegi kongruen.</li>
                <li><b>12 Rusuk:</b> Memiliki panjang yang sama besar ($s$).</li>
                <li><b>8 Titik Sudut:</b> Titik potong antar 3 rusuk yang saling tegak lurus.</li>
                <li><b>12 Diagonal Bidang & 4 Diagonal Ruang</b></li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_kubus, unsafe_allow_html=True)
        
        card_rumus_kubus = """
        <div class="smk-card-tech">
            <h3>📝 Formulasi Metrik & Diagonal</h3>
        </div>
        """
        st.markdown(card_rumus_kubus, unsafe_allow_html=True)
        
        # --- BAGIAN YANG MENYEBABKAN EROR DI FILE ANDA ---
        st.latex(r"Volume \ (V) = s^3 \quad | \quad Luas \ Permukaan \ (L) = 6s^2")
        st.latex(r"Diagonal \ Bidang \ (D_b) = s\sqrt{2}")
        st.latex(r"Diagonal \ Ruang \ (D_r) = s\sqrt{3}")
