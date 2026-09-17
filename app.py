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
    [
        "Beranda Analisis", 
        "Capaian & Alur (CP & ATP)", 
        "Analisis Kubus", 
        "Analisis Balok", 
        "Analisis Prisma Segitiga",
        "Analisis Limas Segi Empat",
        "Analisis Tabung & Kerucut",
        "Analisis Bola",
        "Analisis Perubahan Ukuran",
        "Proyeksi Jaring-Jaring"
    ]
)

# --- FUNGSI KERANGKA 3D KUBUS & BALOK ---
def get_wireframe_data(x, y, z):
    lines_idx = [
        0,1, 1,2, 2,3, 3,0, 
        4,5, 5,6, 6,7, 7,4, 
        0,4, 1,5, 2,6, 3,7  
    ]
    x_lines, y_lines, z_lines = [], [], []
    for i in range(0, len(lines_idx), 2):
        p1, p2 = lines_idx[i], lines_idx[i+1]
        x_lines.extend([x[p1], x[p2], None])
        y_lines.extend([y[p1], y[p2], None])
        z_lines.extend([z[p1], z[p2], None])
    return x_lines, y_lines, z_lines

# --- BERANDA ---
if pilihan_menu == "Beranda Analisis":
    col_text, col_img = st.columns([3, 2])
    with col_text:
        st.title("Modul Interaktif Bangun Ruang 🖥️")
        st.markdown("<p style='font-style: italic; color: #6c757d; margin-top: -15px;'>Mata Pelajaran Matematika SMP Kelas 8 (Fase D)</p>", unsafe_allow_html=True)
        st.markdown("### Selamat Datang di Lab-Go 😉")
        st.markdown("Aplikasi pembelajaran interaktif lengkap untuk memahami unsur, jaring-jaring, luas permukaan, volume, hingga analisis perubahan ukuran bangun ruang sisi datar dan sisi lengkung.")
        st.info("👉 Silakan pilih menu di sidebar sebelah kiri untuk mulai mengeksplorasi.")
    with col_img:
        st.write("")
        try:
            st.image("images (4).jpg", use_container_width=True, caption="Media Belajar Matematika SMP")
        except Exception:
            pass
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 13px;'>© 2026 Modul Matematika Kelas 8 SMP | Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)

# --- CAPAIAN & ALUR TUJUAN (CP & ATP) ---
elif pilihan_menu == "Capaian & Alur (CP & ATP)":
    st.title("🎯 Capaian Pembelajaran & Alur Tujuan Pembelajaran")
    st.markdown("Berikut adalah landasan kurikulum yang digunakan dalam pengembangan modul interaktif ini.")
    
    st.markdown("""
    <div class="smp-card">
        <h3>📌 Capaian Pembelajaran (CP) - Elemen Geometri (Fase D)</h3>
        <p>Peserta didik dapat menjelaskan cara untuk menentukan luas permukaan dan volume bangun ruang (prisma, tabung, limas, kerucut, dan bola) serta dapat menyelesaikan masalah kontekstual yang berkaitan. Peserta didik juga dapat menjelaskan pengaruh perubahan secara proporsional dari bangun ruang terhadap ukuran panjang, luas, dan/atau volume.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Alur Tujuan Pembelajaran (ATP)")
    
    tab1, tab2, tab3, tab4 = st.tabs(["1️⃣ Sisi Datar", "2️⃣ Luas & Volume Sisi Datar", "3️⃣ Sisi Lengkung", "4️⃣ Analisis Perubahan"])
    
    with tab1:
        st.markdown("#### Mengenal Bangun Ruang Sisi Datar")
        st.markdown("* Mengidentifikasi unsur-unsur kubus, balok, prisma, dan limas (titik sudut, rusuk, sisi, diagonal bidang, dan bidang diagonal).")
        st.markdown("* Membuat jaring-jaring kubus, balok, prisma, dan limas.")
        
    with tab2:
        st.markdown("#### Menghitung Luas Permukaan dan Volume Bangun Ruang Sisi Datar")
        st.markdown("* Menurunkan rumus luas permukaan kubus, balok, prisma, dan limas.")
        st.markdown("* Menghitung luas permukaan gabungan atau bangun ruang sisi datar tunggal.")
        st.markdown("* Menurunkan rumus volume kubus, balok, prisma, dan limas.")
        st.markdown("* Menghitung volume bangun ruang sisi datar.")
        
    with tab3:
        st.markdown("#### Mengenal Bangun Ruang Sisi Lengkung")
        st.markdown("* Mengidentifikasi unsur-unsur tabung, kerucut, dan bola.")
        st.markdown("* Membuat jaring-jaring tabung dan kerucut.")
        st.markdown("* Menghitung luas permukaan dan volume tabung, kerucut, serta bola.")
        
    with tab4:
        st.markdown("#### Analisis Perubahan Ukuran")
        st.markdown("* Menjelaskan pengaruh perubahan ukuran panjang (skala) terhadap luas permukaan dan volume bangun ruang.")

# --- KUBUS ---
elif pilihan_menu == "Analisis Kubus":
    st.title("🧊 Eksplorasi Kubus")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Kubus</h3>
            <ul>
                <li><b>Sisi:</b> 6 buah persegi kongruen.</li>
                <li><b>Rusuk:</b> 12 rusuk sama panjang.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"Volume \ (V) = s^3")
        st.latex(r"Luas \ Permukaan \ (L_p) = 6 \times s^2")
        
        sisi = st.number_input("Masukkan Panjang Sisi Kubus (s):", min_value=1, value=5, step=1, format="%d")
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        
        with st.expander("1️⃣ Langkah Menghitung Volume", expanded=True):
            st.markdown("* **Rumus:** $V = s \\times s \\times s$")
            st.markdown(f"* **Penyelesaian:** $V = {sisi} \\times {sisi} \\times {sisi}$")
            st.markdown(f"* **Hasil Akhir:** {volume} satuan kubik")
            
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
            st.markdown("* **Rumus:** $L_p = 6 \\times (s \\times s)$")
            st.markdown(f"* **Penyelesaian:** $L_p = 6 \\times ({sisi} \\times {sisi}) = 6 \\times {sisi**2}$")
            st.markdown(f"* **Hasil Akhir:** {luas_permukaan} satuan persegi")

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

# --- BALOK ---
elif pilihan_menu == "Analisis Balok":
    st.title("🧱 Eksplorasi Balok")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Balok</h3>
            <ul>
                <li><b>Sisi:</b> 6 sisi persegi panjang (3 pasang berhadapan).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"Volume \ (V) = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L_p) = 2 \times (p \cdot l + p \cdot t + l \cdot t)")
        
        p = st.number_input("Masukkan Panjang (p):", min_value=1, value=6, step=1, format="%d")
        l = st.number_input("Masukkan Lebar (l):", min_value=1, value=4, step=1, format="%d")
        t = st.number_input("Masukkan Tinggi (t):", min_value=1, value=3, step=1, format="%d")
        
        v_balok = p * l * t
        lp_balok = 2 * (p*l + p*t + l*t)
        
        with st.expander("1️⃣ Langkah Menghitung Volume", expanded=True):
            st.markdown("* **Rumus:** $V = p \\times l \\times t$")
            st.markdown(f"* **Penyelesaian:** $V = {p} \\times {l} \\times {t}$")
            st.markdown(f"* **Hasil Akhir:** {v_balok} satuan kubik")
            
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
            st.markdown("* **Rumus:** $L_p = 2 \\times (p\\cdot l + p\\cdot t + l\\cdot t)$")
            st.markdown(f"* **Penyelesaian:** $L_p = 2 \\times (({p}\\times{l}) + ({p}\\times{t}) + ({l}\\times{t}))$")
            st.markdown(f"* **Hasil Akhir:** {lp_balok} satuan persegi")

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

# --- PRISMA SEGITIGA ---
elif pilihan_menu == "Analisis Prisma Segitiga":
    st.title("⛺ Eksplorasi Prisma Segitiga")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Prisma Segitiga</h3>
            <ul>
                <li><b>Alas & Atap:</b> Berbentuk segitiga yang kongruen dan sejajar.</li>
                <li><b>Sisi Tegak:</b> Berbentuk 3 buah bidang persegi panjang.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = \text{Luas Alas} \times \text{Tinggi Prisma}")
        st.latex(r"Luas \ Permukaan \ (L_p) = (2 \times \text{Luas Alas}) + (\text{Keliling Alas} \times \text{Tinggi Prisma})")
        
        alas_tri = st.number_input("Panjang Alas Segitiga (a):", min_value=1.0, value=4.0, step=1.0)
        tinggi_tri = st.number_input("Tinggi Alas Segitiga (t_alas):", min_value=1.0, value=3.0, step=1.0)
        sisi_miring_alas = st.number_input("Sisi Miring Alas Segitiga / Sisi Lainnya:", min_value=1.0, value=5.0, step=1.0)
        tinggi_pris = st.number_input("Tinggi Prisma (t_prisma):", min_value=1.0, value=6.0, step=1.0)
        
        luas_alas = 0.5 * alas_tri * tinggi_tri
        keliling_alas = alas_tri + tinggi_tri + sisi_miring_alas
        v_prisma = luas_alas * tinggi_pris
        lp_prisma = (2 * luas_alas) + (keliling_alas * tinggi_pris)
        
        with st.expander("1️⃣ Langkah Menghitung Volume", expanded=True):
            st.markdown("* **Rumus:** $V = \\text{Luas Alas} \\times \\text{Tinggi Prisma}$")
            st.markdown(f"* **Hitung Luas Alas:** $\\frac{{1}}{{2}} \\times a \\times t_{{alas}} = \\frac{{1}}{{2}} \\times {alas_tri} \\times {tinggi_tri} = {luas_alas}$")
            st.markdown(f"* **Penyelesaian:** $V = {luas_alas} \\times {tinggi_pris}$")
            st.markdown(f"* **Hasil Akhir:** {v_prisma:.2f} satuan kubik")
            
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
            st.markdown("* **Rumus:** $L_p = (2 \\times \\text{Luas Alas}) + (\\text{Keliling Alas} \\times \\text{Tinggi Prisma})$")
            st.markdown(f"* **Hitung Keliling Alas:** ${alas_tri} + {tinggi_tri} + {sisi_miring_alas} = {keliling_alas}$")
            st.markdown(f"* **Penyelesaian:** $L_p = (2 \\times {luas_alas}) + ({keliling_alas} \\times {tinggi_pris})$")
            st.markdown(f"* **Hasil Akhir:** {lp_prisma:.2f} satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Prisma Segitiga")
        xa, ya, za = 0.0, 0.0, 0.0               
        xb, yb, zb = float(alas_tri), 0.0, 0.0      
        xc, yc, zc = 0.0, float(tinggi_tri), 0.0   
        xd, yd, zd = 0.0, 0.0, float(tinggi_pris)               
        xe, ye, ze = float(alas_tri), 0.0, float(tinggi_pris)      
        xf, yf, zf = 0.0, float(tinggi_tri), float(tinggi_pris)   
        
        x_pts = [xa, xb, xc, xd, xe, xf]
        y_pts = [ya, yb, yc, yd, ye, yf]
        z_pts = [za, zb, zc, zd, ze, zf]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x_pts, y=y_pts, z=z_pts,
                i=[0, 0, 0, 3, 3, 1],
                j=[1, 2, 3, 4, 5, 2],
                k=[2, 3, 4, 5, 4, 5],
                color='#ffc107', opacity=0.35, flatshading=True
            ),
            go.Scatter3d(
                x=[xa, xb, xc, xa, xd, xe, xf, xd, xa, xd, xb, xe, xc, xf],
                y=[ya, yb, yc, ya, yd, ye, yf, yd, ya, yd, yb, ye, yc, yf],
                z=[za, zb, zc, za, zd, ze, zf, zd, za, zd, zb, ze, zc, zf],
                mode='lines',
                line=dict(color='black', width=4)
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(range=[-1, alas_tri+2], title='X'),
                yaxis=dict(range=[-1, tinggi_tri+2], title='Y'),
                zaxis=dict(range=[-1, tinggi_pris+2], title='Z')
            ), 
            margin=dict(l=0, r=0, b=0, t=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# --- LIMAS SEGI EMPAT ---
elif pilihan_menu == "Analisis Limas Segi Empat":
    st.title("📐 Eksplorasi Limas Segi Empat")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik Limas Segi Empat</h3>
            <ul>
                <li><b>Alas:</b> Berbentuk persegi / persegi panjang.</li>
                <li><b>Sisi Tegak:</b> Berbentuk segitiga yang bertemu di satu titik puncak.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = \frac{1}{3} \times \text{Luas Alas} \times \text{Tinggi}")
        st.latex(r"Luas \ Permukaan = \text{Luas Alas} + \text{Jumlah Luas Sisi Tegak}")
        
        s_alas = st.number_input("Sisi Alas Persegi (s):", min_value=1.0, value=4.0, step=1.0)
        t_limas = st.number_input("Tinggi Limas (t):", min_value=1.0, value=6.0, step=1.0)
        
        luas_alas = s_alas ** 2
        v_limas = (1/3) * luas_alas * t_limas
        sisi_tegak_t = np.sqrt((s_alas / 2)**2 + t_limas**2)
        luas_sisi_tegak = 4 * (0.5 * s_alas * sisi_tegak_t)
        lp_limas = luas_alas + luas_sisi_tegak
        
        with st.expander("1️⃣ Langkah Menghitung Volume", expanded=True):
            st.markdown("* **Rumus:** $V = \\frac{1}{3} \\times \\text{Luas Alas} \\times \\text{Tinggi}$")
            st.markdown(f"* **Hitung Luas Alas:** ${s_alas} \\times {s_alas} = {luas_alas}$")
            st.markdown(f"* **Penyelesaian:** $V = \\frac{{1}}{{3}} \\times {luas_alas} \\times {t_limas}$")
            st.markdown(f"* **Hasil Akhir:** {v_limas:.2f} satuan kubik")
            
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
            st.markdown("* **Rumus:** $L_p = \\text{Luas Alas} + (4 \\times \\text{Luas Segitiga Sisi Tegak})$")
            st.markdown(f"* **Tinggi Sisi Tegak ($t_s$):** $\\sqrt{{({s_alas}/2)^2 + {t_limas}^2}} = {sisi_tegak_t:.2f}$")
            st.markdown(f"* **Penyelesaian:** $L_p = {luas_alas} + (4 \\times \\frac{{1}}{{2}} \\times {s_alas} \\times {sisi_tegak_t:.2f})$")
            st.markdown(f"* **Hasil Akhir:** {lp_limas:.2f} satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Limas")
        sf = float(s_alas)
        tf = float(t_limas)
        xlm = [0, sf, sf, 0, sf/2]
        ylm = [0, 0, sf, sf, sf/2]
        zlm = [0, 0, 0, 0, tf]
        fig = go.Figure(data=[go.Mesh3d(
            x=xlm, y=ylm, z=zlm,
            i=[0, 0, 0, 1, 1],
            j=[1, 2, 4, 2, 4],
            k=[2, 3, 4, 3, 2],
            color='#dc3545', opacity=0.6, flatshading=True
        )])
        fig.update_layout(scene=dict(xaxis=dict(range=[-1, sf+1]), yaxis=dict(range=[-1, sf+1]), zaxis=dict(range=[-1, tf+1])), margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- TABUNG & KERUCUT ---
elif pilihan_menu == "Analisis Tabung & Kerucut":
    st.title("🥫 Eksplorasi Tabung & Kerucut (Sisi Lengkung)")
    pilih_sisi_lengkung = st.radio("Pilih Bangun:", ["Tabung", "Kerucut"], horizontal=True)
    
    if pilih_sisi_lengkung == "Tabung":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Tabung (Cylinder)")
            st.latex(r"V = \pi \times r^2 \times t")
            st.latex(r"L_p = 2 \times \pi \times r \times (r + t)")
            
            r_tab = st.number_input("Jari-jari (r):", min_value=1.0, value=7.0, step=1.0)
            t_tab = st.number_input("Tinggi Tabung (t):", min_value=1.0, value=10.0, step=1.0)
            
            v_tab = np.pi * (r_tab**2) * t_tab
            lp_tab = 2 * np.pi * r_tab * (r_tab + t_tab)
            
            with st.expander("1️⃣ Langkah Menghitung Volume Tabung", expanded=True):
                st.markdown("* **Rumus:** $V = \\pi \\times r^2 \\times t$")
                st.markdown(f"* **Penyelesaian:** $V = \\frac{{22}}{{7}} \\times {r_tab}^2 \\times {t_tab}$")
                st.markdown(f"* **Hasil Akhir:** {v_tab:.2f} satuan kubik")
                
            with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Tabung", expanded=True):
                st.markdown("* **Rumus:** $L_p = 2 \\times \\pi \\times r \\times (r + t)$")
                st.markdown(f"* **Penyelesaian:** $L_p = 2 \\times \\frac{{22}}{{7}} \\times {r_tab} \\times ({r_tab} + {t_tab})$")
                st.markdown(f"* **Hasil Akhir:** {lp_tab:.2f} satuan persegi")
                
        with col2:
            st.markdown("### 💡 Catatan Unsur Tabung")
            st.markdown("* Memiliki 2 buah rusuk lengkung.")
            st.markdown("* Sisi alas dan tutup berbentuk lingkaran yang kongruen.")
            
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Kerucut (Cone)")
            st.latex(r"V = \frac{1}{3} \times \pi \times r^2 \times t")
            st.latex(r"L_p = \pi \times r \times (r + s)")
            
            r_ker = st.number_input("Jari-jari Alas (r):", min_value=1.0, value=3.0, step=1.0)
            t_ker = st.number_input("Tinggi Kerucut (t):", min_value=1.0, value=4.0, step=1.0)
            
            s_pelukis = np.sqrt(r_ker**2 + t_ker**2)
            v_ker = (1/3) * np.pi * (r_ker**2) * t_ker
            lp_ker = np.pi * r_ker * (r_ker + s_pelukis)
            
            with st.expander("1️⃣ Langkah Menghitung Volume Kerucut", expanded=True):
                st.markdown("* **Rumus:** $V = \\frac{1}{3} \\times \\pi \\times r^2 \\times t$")
                st.markdown(f"* **Penyelesaian:** $V = \\frac{{1}}{{3}} \\times \\pi \\times {r_ker}^2 \\times {t_ker}$")
                st.markdown(f"* **Hasil Akhir:** {v_ker:.2f} satuan kubik")
                
            with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Kerucut", expanded=True):
                st.markdown("* **Rumus:** $L_p = \\pi \\times r \\times (r + s)$")
                st.markdown(f"* **Cari Garis Pelukis ($s$):** $\\sqrt{{r^2 + t^2}} = \\sqrt{{{r_ker}^2 + {t_ker}^2}} = {s_pelukis:.2f}$")
                st.markdown(f"* **Penyelesaian:** $L_p = \\pi \\times {r_ker} \\times ({r_ker} + {s_pelukis:.2f})$")
                st.markdown(f"* **Hasil Akhir:** {lp_ker:.2f} satuan persegi")
                
        with col2:
            st.markdown("### 💡 Catatan Unsur Kerucut")
            st.markdown("* Memiliki 1 buah sisi alas berbentuk lingkaran dan 1 sisi selimut.")
            st.markdown("* Garis pelukis ($s$) dihitung dengan teorema Pythagoras.")

# --- BOLA ---
elif pilihan_menu == "Analisis Bola":
    st.title("⚽ Eksplorasi Bola")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik Bola</h3>
            <ul>
                <li>Hanya memiliki 1 buah sisi melengkung tertutup.</li>
                <li>Tidak memiliki titik sudut dan rusuk.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"V = \frac{4}{3} \times \pi \times r^3")
        st.latex(r"L_p = 4 \times \pi \times r^2")
        
        r_bol = st.number_input("Jari-jari Bola (r):", min_value=1.0, value=7.0, step=1.0)
        v_bol = (4/3) * np.pi * (r_bol**3)
        lp_bol = 4 * np.pi * (r_bol**2)
        
        with st.expander("1️⃣ Langkah Menghitung Volume Bola", expanded=True):
            st.markdown("* **Rumus:** $V = \\frac{4}{3} \\times \\pi \\times r^3$")
            st.markdown(f"* **Penyelesaian:** $V = \\frac{{4}}{{3}} \\times \\pi \\times {r_bol}^3$")
            st.markdown(f"* **Hasil Akhir:** {v_bol:.2f} satuan kubik")
            
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Bola", expanded=True):
            st.markdown("* **Rumus:** $L_p = 4 \\times \\pi \\times r^2$")
            st.markdown(f"* **Penyelesaian:** $L_p = 4 \\times \\pi \\times {r_bol}^2$")
            st.markdown(f"* **Hasil Akhir:** {lp_bol:.2f} satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Bola")
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 30)
        x_b = r_bol * np.outer(np.cos(u), np.sin(v))
        y_b = r_bol * np.outer(np.sin(u), np.sin(v))
        z_b = r_bol * np.outer(np.ones(np.size(u)), np.cos(v))
        fig = go.Figure(data=[go.Surface(x=x_b, y=y_b, z=z_b, colorscale='Blues')])
        fig.update_layout(scene=dict(xaxis=dict(range=[-10, 10]), yaxis=dict(range=[-10, 10]), zaxis=dict(range=[-10, 10])), margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- ANALISIS PERUBAHAN UKURAN ---
elif pilihan_menu == "Analisis Perubahan Ukuran":
    st.title("📈 Analisis Pengaruh Perubahan Skala/Ukuran")
    st.markdown("Sesuai CP Fase D: Menjelaskan pengaruh perubahan secara proporsional dari bangun ruang terhadap ukuran panjang, luas, dan/atau volume.")
    
    skala = st.slider("Pilih Faktor Skala Perubahan ($k$):", min_value=1.0, max_value=5.0, value=2.0, step=0.5)
    
    st.markdown(f"""
    <div class="smp-card">
        <h3>🔍 Aturan Perubahan Skala (Faktor Skala = {skala})</h3>
        <ul>
            <li><b>Panjang/Rusuk/Jari-jari:</b> Berubah sebesar $\\times {skala}$ ($k = {skala}$)</li>
            <li><b>Luas Permukaan:</b> Berubah sebesar $\\times {skala**2}$ ($k^2 = {skala**2}$)</li>
            <li><b>Volume:</b> Berubah sebesar $\\times {skala**3:.1f}$ ($k^3 = {skala**3:.1f}$)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 💡 Contoh Kasus pada Kubus:")
    s_awal = 3
    v_awal = s_awal**3
    lp_awal = 6 * (s_awal**2)
    
    s_akhir = s_awal * skala
    v_akhir = s_akhir**3
    lp_akhir = 6 * (s_akhir**2)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Sebelum Skala ($s = {s_awal}$):**")
        st.write(f"- Luas Permukaan: {lp_awal}")
        st.write(f"- Volume: {v_awal}")
    with col2:
        st.markdown(f"**Sesudah Diperbesar ($s = {s_akhir}$):**")
        st.write(f"- Luas Permukaan: {lp_akhir} (Naik {skala**2} kali)")
        st.write(f"- Volume: {v_akhir} (Naik {skala**3:.1f} kali)")

# --- PROYEKSI JARING-JARING ---
elif pilihan_menu == "Proyeksi Jaring-Jaring":
    st.title("📦 Proyeksi Berbagai Variasi Jaring-Jaring")
    st.markdown("Pilih jenis bangun ruang dan variasi pola jaring-jaring 2 dimensi.")
    
    pilihan_bangun = st.radio("Pilih Bangun Ruang:", ["Jaring-Jaring Kubus (Persegi)", "Jaring-Jaring Balok (Persegi Panjang)"], horizontal=True)
    
    fig_net = go.Figure()
    
    if "Kubus" in pilihan_bangun:
        variasi_kubus = st.selectbox(
            "Pilih Variasi Pola Jaring-Jaring Kubus:",
            [
                "Variasi 1 (Pola Salib / Cross)", 
                "Variasi 2 (Pola Huruf L / Tangga)", 
                "Variasi 3 (Pola Zig-Zag Samping)", 
                "Variasi 4 (Pola Geser Berjajar)"
            ]
        )
        
        if variasi_kubus == "Variasi 1 (Pola Salib / Cross)":
            shapes_list = [
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=2, x1=2, y1=3, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=3, x1=2, y1=4, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=0, y0=1, x1=1, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
            ]
        elif variasi_kubus == "Variasi 2 (Pola Huruf L / Tangga)":
            shapes_list = [
                dict(type="rect", x0=0, y0=0, x1=1, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=0, x1=3, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=2, x1=3, y1=3, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=3, y0=1, x1=4, y1=2, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
            ]
        elif variasi_kubus == "Variasi 3 (Pola Zig-Zag Samping)":
            shapes_list = [
                dict(type="rect", x0=0, y0=2, x1=1, y1=3, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=0, y0=1, x1=1, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=2, y0=0, x1=3, y1=1, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=3, y0=0, x1=4, y1=1, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
            ]
        else:
            shapes_list = [
                dict(type="rect", x0=0, y0=0, x1=1, y1=1, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
                dict(type="rect", x0=2, y0=0, x1=3, y1=1, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
                dict(type="rect", x0=3, y0=1, x1=4, y1=2, line=dict(color="blue", width=2), fillcolor="#ffe69c", opacity=0.8),
            ]
            
        fig_net.update_layout(
            title=f"Proyeksi 2D - {variasi_kubus}",
            xaxis=dict(range=[-1, 5], showgrid=True, zeroline=False, scaleanchor="y", scaleratio=1),
            yaxis=dict(range=[-1, 5], showgrid=True, zeroline=False),
            width=500, height=500,
            shapes=shapes_list
        )
        st.plotly_chart(fig_net, use_container_width=True)
        
    else:
        variasi_balok = st.selectbox(
            "Pilih Variasi Pola Jaring-Jaring Balok:",
            [
                "Variasi 1 (Pola Salib Panjang)", 
                "Variasi 2 (Pola T-Shape / Terpusat)"
            ]
        )
        
        if variasi_balok == "Variasi 1 (Pola Salib Panjang)":
            shapes_balok = [
                dict(type="rect", x0=1, y0=1.5, x1=3, y1=3, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
                dict(type="rect", x0=1, y0=0, x1=3, y1=1.5, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
                dict(type="rect", x0=1, y0=3, x1=3, y1=4.5, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
                dict(type="rect", x0=1, y0=4.5, x1=3, y1=6, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
                dict(type="rect", x0=0, y0=1.5, x1=1, y1=3, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
                dict(type="rect", x0=3, y0=1.5, x1=4, y1=3, line=dict(color="green", width=2), fillcolor="#d1e7dd", opacity=0.8), 
            ]
            x_range, y_range = [-1, 5], [-1, 7]
        else:
            shapes_balok = [
                dict(type="rect", x0=1, y0=1.5, x1=3, y1=3, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
                dict(type="rect", x0=1, y0=0, x1=3, y1=1.5, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
                dict(type="rect", x0=1, y0=3, x1=3, y1=4.5, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
                dict(type="rect", x0=3, y0=1.5, x1=5, y1=3, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
                dict(type="rect", x0=5, y0=1.5, x1=7, y1=3, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
                dict(type="rect", x0=-1, y0=1.5, x1=1, y1=3, line=dict(color="green", width=2), fillcolor="#cfe2ff", opacity=0.8), 
            ]
            x_range, y_range = [-2, 8], [-1, 5]
            
        fig_net.update_layout(
            title=f"Proyeksi 2D - {variasi_balok}",
            xaxis=dict(range=x_range, showgrid=True, zeroline=False),
            yaxis=dict(range=y_range, showgrid=True, zeroline=False),
            width=550, height=500,
            shapes=shapes_balok
        )
        st.plotly_chart(fig_net, use_container_width=True)

# --- FOOTER SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.caption("Pengembang: Mochammad Rifqi Al Khadziq")
