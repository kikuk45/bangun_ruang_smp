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
        # Gambar ilustrasi bisa disesuaikan, atau biarkan kosong jika ingin fokus ke materi teknis
        st.info("💡 **Tips Pembelajaran:** Gunakan fitur *rotate* dan *zoom* pada grafis 3D untuk melihat hubungan antar titik sudut secara lebih presisi.")

# --- HALAMAN: KUBUS ---
elif menu == "🧊 Analisis Kubus":
    st.title("🧊 Analisis Geometri Ruang: Kubus (Hexahedron)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""<div class="smk-card">
            <h3>📋 Elemen Struktur Kubus</h3>
            <ul>
                <li><b>6 Sisi (Bidang):</b> Seluruhnya berbentuk persegi kongruen.</li>
                <li><b>12 Rusuk:</b> Memiliki panjang yang sama besar ($s$).</li>
                <li><b>8 Titik Sudut:</b> Titik potong antar 3 rusuk yang saling tegak lurus.</li>
                <li><b>12 Diagonal Bidang & 4 Diagonal Ruang</b></li>
            </ul>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("""<div class="smk-card-tech">
            <h3>📝 Formulasi Metrik & Diagonal</h3>
        </div>""", unsafe_allow_html=True)
        st.latex(r"Volume \ (V) = s^3 \quad | \quad Luas \ Permukaan \ (L) = 6s^2")
        st.latex(r"Diagonal \ Bidang \ (D_b) = s\sqrt{2}")
        st.latex(r"Diagonal \ Ruang \ (D_r) = s\sqrt{3}")
        
        st.markdown("### 🧮 Lab Parameter Digital")
        sisi = st.number_input("Input Panjang Sisi Kubus (s):", min_value=1.0, value=5.0, step=1.0)
        
        # Perhitungan Metrik
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        diag_bidang = sisi * np.sqrt(2)
        diag_ruang = sisi * np.sqrt(3)
        
        st.success(f"📊 **Hasil Analisis Struktur (s = {sisi}):**\n\n"
                   f"🔹 **Volume (V):** {volume:.2f} satuan kubik\n\n"
                   f"🔹 **Luas Permukaan (L):** {luas_permukaan:.2f} satuan persegi\n\n"
                   f"◼️ **Panjang Diagonal Bidang ($s\sqrt{{2}}$):** {diag_bidang:.4f} satuan\n\n"
                   f"🚀 **Panjang Diagonal Ruang ($s\sqrt{{3}}$):** {diag_ruang:.4f} satuan")

    with col2:
        st.markdown("### 🌐 Model Proyeksi 3D")
        st.caption("Gunakan kursor untuk memutar, menggeser, atau memperbesar proyeksi kubus.")
        
        s = sisi
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        # Ambil data kerangka garis
        xl, yl, zl = get_wireframe_data(x, y, z)
        
        fig = go.Figure()
        
        # Plot Objek 3D (Solid transparan)
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.3,
            color='#0d6efd',
            flatshading=True,
            name="Volume"
        ))
        
        # Plot Kerangka (Wireframe agar garis terlihat jelas untuk anak SMK)
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl,
            mode='lines',
            line=dict(color='#0d6efd', width=4),
            name="Rusuk"
        ))
        
        # Plot Label Titik Sudut
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers+text',
            text=labels,
            textposition="top center",
            marker=dict(size=6, color='black'),
            name="Titik Sudut"
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X (Sisi)', range=[-1, s+2], backgroundcolor="#f8f9fa"),
                yaxis=dict(title='Y (Sisi)', range=[-1, s+2], backgroundcolor="#f8f9fa"),
                zaxis=dict(title='Z (Sisi)', range=[-1, s+2], backgroundcolor="#f8f9fa")
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN: BALOK ---
elif menu == "🧱 Analisis Balok":
    st.title("🧱 Analisis Geometri Ruang: Balok (Prisma Tegak Segiempat)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""<div class="smk-card">
            <h3>📋 Karakteristik Struktur Balok</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 3 pasang bidang berbentuk persegi panjang yang saling berhadapan dan kongruen.</li>
                <li><b>Dimensi Utama:</b> Ditentukan oleh variabel Panjang ($p$), Lebar ($l$), dan Tinggi ($t$).</li>
                <li><b>Sifat Tegak Lurus:</b> Setiap rusuk yang bertemu di satu titik sudut saling membentuk sudut $90^\circ$.</li>
