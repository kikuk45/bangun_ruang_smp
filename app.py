import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Modul Bangun Ruang Kelas 8 SMP", 
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
    .smp-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 6px solid #0d6efd;
        margin-bottom: 20px;
    }
    .smp-card-tech {
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
    <h2 style='margin-bottom: 0;'>📐 Lab Bangun Ruang</h2>
    <p style='color: #6c757d; font-size: 14px;'>Kurikulum Merdeka / K-13 Kelas 8 SMP</p>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

pilihan_menu = st.sidebar.selectbox(
    "Pilih Menu Pembelajaran:", 
    ["Beranda Analisis", "Analisis Kubus", "Analisis Balok", "Proyeksi Jaring-Jaring"]
)

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
if pilihan_menu == "Beranda Analisis":
    col_text, col_img = st.columns([3, 2])
    
    with col_text:
        st.title("Modul Interaktif Bangun Ruang Sisi Datar 🖥️")
        st.markdown("<p style='font-style: italic; color: #6c757d; margin-top: -15px;'>Mata Pelajaran Matematika SMP Kelas 8</p>", unsafe_allow_html=True)
        
        st.markdown("### Selamat Datang di LabGo 😉")
        st.markdown("Aplikasi ini disusun khusus berdasarkan capaian pembelajaran Matematika Kelas 8 SMP, yang berfokus pada pengenalan **unsur-unsur**, **jaring-jaring**, **luas permukaan**, dan **volume** untuk bangun ruang sisi datar (Kubus dan Balok).")
        
        st.markdown("**Kompetensi yang Dipelajari di Kelas 8:**")
        st.markdown("* 📋 **Identifikasi Unsur:** Mengenal jumlah sisi, rusuk, titik sudut, dan diagonal sisi/bidang dasar.")
        st.markdown("* 📦 **Jaring-Jaring Bangun Ruang:** Memahami bagaimana bangun ruang dibentuk dari potongan bidang datarnya.")
        st.markdown("* 🧮 **Perhitungan Bertahap:** Mempelajari rumus Volume dan Luas Permukaan secara runtut.")
        st.markdown("* 🌐 **Visualisasi 3D Interaktif:** Membantu siswa membayangkan bentuk nyata kubus dan balok dari berbagai sudut.")
        st.write("")
        st.info("👉 Silakan pilih menu di sidebar sebelah kiri untuk mulai mengeksplorasi.")
        
    with col_img:
        st.write("")
        try:
            st.image("images (4).jpg", use_container_width=True, caption="Media Belajar Matematika SMP")
        except Exception:
            st.info("💡 **Tips Guru/Siswa:** Gunakan rincian langkah pengerjaan di bawah kalkulator untuk menuliskan catatan di buku catatan matematika.")
            
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 13px;'>© 2026 Modul Matematika Kelas 8 SMP | Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)

# --- HALAMAN: KUBUS KELAS 8 ---
elif pilihan_menu == "Analisis Kubus":
    st.title("🧊 Eksplorasi Kubus (Matematika Kelas 8)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Kubus (Kelas 8)</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 6 sisi berbentuk persegi yang kongruen (sama besar).</li>
                <li><b>Rusuk:</b> Memiliki 12 rusuk yang sama panjang (<i>s</i>).</li>
                <li><b>Titik Sudut:</b> Memiliki 8 titik sudut.</li>
                <li><b>Jaring-jaring:</b> Terdiri dari 6 buah persegi yang saling terhubung jika dibuka.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_kubus, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = s^3")
        st.latex(r"Luas \ Permukaan \ (L_p) = 6 \times s^2")
        
        st.markdown("### 🧮 Kalkulator Kubus")
        sisi = st.number_input("Masukkan Panjang Sisi Kubus (s):", min_value=1, value=5, step=1, format="%d")
        
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        
        st.markdown("### 📋 Rincian Langkah Pengerjaan:")
        with st.expander("1️⃣ Langkah Menghitung Volume Kubus", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Volume adalah kapasitas ruang kubus.")
            st.markdown(r"* **Rumus:** $V = s \times s \times s$")
            st.markdown(f"* **Hasil Akhir:** **{volume}** satuan kubik")

        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Kubus", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Total luas dari 6 buah sisi persegi.")
            st.markdown(r"* **Rumus:** $L_p = 6 \times (s \times s)$")
            st.markdown(f"* **Hasil Akhir:** **{luas_permukaan}** satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Kubus")
        s = float(sisi)
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        fig.add_trace(go.Mesh3d(x=x, y=y, z=z, i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7], j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3], k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2], opacity=0.20, color='#0d6efd', flatshading=True))
        fig.add_trace(go.Scatter3d(x=xl, y=yl, z=zl, mode='lines', line=dict(color='#343a40', width=4)))
        fig.update_layout(scene=dict(xaxis=dict(range=[-1, s+2]), yaxis=dict(range=[-1, s+2]), zaxis=dict(range=[-1, s+2])), margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN: BALOK KELAS 8 ---
elif pilihan_menu == "Analisis Balok":
    st.title("🧱 Eksplorasi Balok (Matematika Kelas 8)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Balok (Kelas 8)</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 6 sisi persegi panjang (3 pasang berhadapan sejajar).</li>
                <li><b>Rusuk:</b> Terdiri dari Panjang (<i>p</i>), Lebar (<i>l</i>), dan Tinggi (<i>t</i>).</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_balok, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L_p) = 2 \times (p \cdot l + p \cdot t + l \cdot t)")
        
        p = st.number_input("Masukkan Panjang (p):", min_value=1, value=6, step=1, format="%d")
        l = st.number_input("Masukkan Lebar (l):", min_value=1, value=4, step=1, format="%d")
        t = st.number_input("Masukkan Tinggi (t):", min_value=1, value=3, step=1, format="%d")
        
        v_balok = p * l * t
        lp_balok = 2 * (p*l + p*t + l*t)
        
        with st.expander("1️⃣ Langkah Menghitung Volume Balok", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Volume dihitung dengan mengalikan luas alas dengan tinggi balok ($V = \text{Luas Alas} \times t$).")
            st.markdown(f"* **Hasil Akhir:** **{v_balok}** satuan kubik")

        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Balok", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Jumlah dari seluruh 3 pasang sisi berhadapan.")
            st.markdown(f"* **Hasil Akhir:** **{lp_balok}** satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Balok")
        pf, lf, tf = float(p), float(l), float(t)
        x = [0, pf, pf, 0, 0, pf, pf, 0]
        y = [0, 0, lf, lf, 0, 0, lf, lf]
        z = [0, 0, 0, 0, tf, tf, tf, tf]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        fig.add_trace(go.Mesh3d(x=x, y=y, z=z, i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7], j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3], k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2], opacity=0.20, color='#198754', flatshading=True))
        fig.add_trace(go.Scatter3d(x=xl, y=yl, z=zl, mode='lines', line=dict(color='#343a40', width=4)))
        fig.update_layout(scene=dict(xaxis=dict(range=[-1, pf+2]), yaxis=dict(range=[-1, lf+2]), zaxis=dict(range=[-1, tf+2])), margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN BARU: PROYEKSI JARING-JARING ---
elif pilihan_menu == "Proyeksi Jaring-Jaring":
    st.title("📦 Proyeksi Jaring-Jaring Bangun Ruang")
    st.markdown("Menu interaktif ini menunjukkan bentuk bentangan 2 dimensi (jaring-jaring) dari kubus atau balok sebelum dirakit menjadi bangun ruang 3 dimensi.")
    
    pilihan_bangun = st.radio("Pilih Bangun Ruang:", ["Jaring-Jaring Kubus", "Jaring-Jaring Balok"], horizontal=True)
    
    fig_net = go.Figure()
    
    if pilihan_bangun == "Jaring-Jaring Kubus":
        st.info("💡 **Model Jaring-Jaring Kubus (Pola Salib / Cross Pattern):** Tersusun atas 6 buah persegi dengan ukuran sisi yang sama.")
        
        # Koordinat 2D sederhana untuk jaring-jaring kubus pola silang (4 kotak vertikal, 2 kotak di samping)
        # Kotak 1 (Alas), Kotak 2 (Depan), Kotak 3 (Atas), Kotak 4 (Belakang), Kotak 5 (Kiri), Kotak 6 (Kanan)
        # Kita plot menggunakan bentuk persegi 2D menggunakan Scatter/Shapes
        
        fig_net.update_layout(
            title="Proyeksi 2D Jaring-Jaring Kubus",
            xaxis=dict(range=[-1, 5], showgrid=True, zeroline=False),
            yaxis=dict(range=[-1, 5], showgrid=True, zeroline=False),
            width=500, height=500,
            shapes=[
                # Kotak Tengah (Depan) [x0, y0, x1, y1]
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
                # Kotak Bawah (Alas)
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
                # Kotak Atas (Tutup)
                dict(type="rect", x0=1, y0=2, x1=2, y1=3, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
                # Kotak Paling Atas (Belakang)
                dict(type="rect", x0=1, y0=3, x1=2, y1=4, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
                # Kotak Kiri
                dict(type="rect", x0=0, y0=1, x1=1, y1=2, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
                # Kotak Kanan
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="lightblue", opacity=0.5),
            ]
        )
        st.plotly_chart(fig_net, use_container_width=True)
        
    else:
        st.info("💡 **Model Jaring-Jaring Balok:** Terdiri dari 3 pasang sisi persegi panjang yang saling berhadapan dan kongruen.")
        
        fig_net.update_layout(
            title="Proyeksi 2D Jaring-Jaring Balok",
            xaxis=dict(range=[-1, 6], showgrid=True, zeroline=False),
            yaxis=dict(range=[-1, 4], showgrid=True, zeroline=False),
            width=500, height=500,
            shapes=[
                # Pola jaring-jaring balok proporsional
                dict(type="rect", x0=2, y0=1, x1=4, y1=2, line=dict(color="green", width=2), fillcolor="lightgreen", opacity=0.5), # Depan
                dict(type="rect", x0=2, y0=0, x1=4, y1=1, line=dict(color="green", width=2), fillcolor="lightgreen", opacity=0.5), # Alas
                dict(type="rect", x0=2, y0=2, x1=4, y1=3, line=dict(color="green", width=2), fillcolor="lightgreen", opacity=0.5), # Atas
                dict(type="rect", x0=0, y0=1, x1=2, y1=2, line=dict(color="green", width=2), fillcolor="lightgreen", opacity=0.5), # Kiri
                dict(type="rect", x0=4, y0=1, x1=6, y1=2, line=dict(color="green", width=2), fillcolor="lightgreen", opacity=0.5), # Kanan
            ]
        )
        st.plotly_chart(fig_net, use_container_width=True)

# --- FOOTER SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.caption("Pengembang: Mochammad Rifqi Al Khadziq")
