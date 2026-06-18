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
        ### Selamat Datang di Modul Geometri Ruang SMK!
        Aplikasi ini dirancang sebagai alat bantu visualisasi objek 3 dimensi guna mempermudah pemahaman konsep kedudukan titik, garis, dan bidang, serta perhitungan jarak dan sudut pada materi **Dimensi Tiga**.
        
        **Fitur Utama Laboratorium Virtual:**
        * 🌐 **Visualisasi Spasial Dinamis:** Manipulasi sudut pandang objek 3D secara *real-time* untuk memperkuat kemampuan spasial (membayangkan ruang).
        * 📊 **Kalkulator Struktur Geometri:** Analisis otomatis ukuran dasar, luas permukaan, volume, hingga panjang **Diagonal Bidang** dan **Diagonal Ruang**.
        * 🔍 **X-Ray Diagonal Simulator:** Gambar komponen garis diagonal ruang secara interaktif langsung pada objek untuk simulasi teorema Pythagoras ruang.
        
        *Silakan pilih menu objek di sebelah kiri untuk memulai analisis.*
        """)
        
    with col_img:
        st.write("")
        # --- MODIFIKASI DISINI: MENAMPILKAN GAMBAR DARI GITHUB ---
        # Ganti URL di bawah ini dengan tautan RAW gambar GitHub kamu sendiri
        url_gambar_github = "images (2).png"
        
        try:
            st.image(url_gambar_github, use_container_width=True, caption="Media Pembelajaran Dimensi Tiga")
        except Exception as e:
            # Sebagai cadangan jika internet bermasalah atau URL salah
            st.info("💡 **Tips Pembelajaran SMK:** Aktifkan fitur garis diagonal pada menu eksperimen untuk membantu visualisasi segitiga siku-siku di dalam ruang saat menghitung jarak titik ke titik.")
# --- HALAMAN: KUBUS ---
elif menu == "🧊 Analisis Kubus":
    st.title("🧊 Analisis Geometri Ruang: Kubus")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="smk-card">
            <h3>📋 Elemen Struktur Kubus</h3>
            <ul>
                <li><b>6 Sisi (Bidang):</b> Seluruhnya berbentuk persegi kongruen (ABCD, EFGH, dst).</li>
                <li><b>12 Rusuk:</b> Memiliki panjang yang sama besar ($s$).</li>
                <li><b>8 Titik Sudut:</b> Titik potong standar notasi geometri ruang.</li>
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
        
        st.latex(r"Volume \ (V) = s^3 \quad | \quad Luas \ Permukaan \ (L) = 6s^2")
        st.latex(r"Diagonal \ Bidang \ (D_b) = s\sqrt{2}")
        st.latex(r"Diagonal \ Ruang \ (D_r) = s\sqrt{3}")
        
        st.markdown("### 🧮 Lab Parameter Digital")
        sisi = st.number_input("Input Panjang Sisi Kubus (s):", min_value=1.0, value=5.0, step=1.0)
        
        st.markdown("##### 🔍 Proyeksi Garis Ruang (Interaktif)")
        show_db = st.checkbox("Tampilkan Diagonal Bidang AC (Alas)")
        show_dr = st.checkbox("Tampilkan Diagonal Ruang AG")
        
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
        st.markdown("### 🌐 Model Proyeksi 3D Interaktif")
        st.caption("Gunakan mouse/kursor untuk memutar (rotate) kubus guna menganalisis letak garis.")
        
        s = sisi
        # Titik sudut koordinat: A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        
        # Plot Objek 3D Transparan
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.15, color='#0d6efd', flatshading=True, name="Volume"
        ))
        
        # Plot Kerangka Utama (Rusuk)
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#495057', width=3), name="Rusuk"
        ))
        
        # INTERAKSI VISUAL: Diagonal Bidang AC
        if show_db:
            fig.add_trace(go.Scatter3d(
                x=[0, s], y=[0, s], z=[0, 0], mode='lines+markers',
                line=dict(color='#dc3545', width=5, dash='dash'),
                marker=dict(size=4), name="Diag. Bidang AC"
            ))
            
        # INTERAKSI VISUAL: Diagonal Ruang AG
        if show_dr:
            fig.add_trace(go.Scatter3d(
                x=[0, s], y=[0, s], z=[0, s], mode='lines+markers',
                line=dict(color='#ffc107', width=6),
                marker=dict(size=4), name="Diag. Ruang AG"
            ))
        
        # Label Titik Sudut Standar (A,B,C,D bawah | E,F,G,H atas)
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z, mode='markers+text',
            text=labels, textposition="top center",
            marker=dict(size=6, color='black'), name="Titik"
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X', range=[-1, s+2]),
                yaxis=dict(title='Y', range=[-1, s+2]),
                zaxis=dict(title='Z', range=[-1, s+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN: BALOK ---
elif menu == "🧱 Analisis Balok":
    st.title("🧱 Analisis Geometri Ruang: Balok")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="smk-card">
            <h3>📋 Karakteristik Struktur Balok</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 3 pasang bidang segiempat berhadapan yang sejajar dan kongruen.</li>
                <li><b>Dimensi:</b> Ditentukan oleh nilai Panjang ($p$), Lebar ($l$), dan Tinggi ($t$).</li>
                <li><b>Diagonal Bidang:</b> Bernilai variatif tergantung bidang mana yang ditinjau.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_balok, unsafe_allow_html=True)
        
        card_rumus_balok = """
        <div class="smk-card-tech">
            <h3>📝 Formulasi Metrik & Diagonal Balok</h3>
        </div>
        """
        st.markdown(card_rumus_balok, unsafe_allow_html=True)
        
        st.latex(r"Volume = p \times l \times t \quad | \quad L_p = 2(pl + pt + lt)")
        st.latex(r"Diag. \ Bidang \ Alas \ (AC) = \sqrt{p^2 + l^2}")
        st.latex(r"Diagonal \ Ruang \ (AG) = \sqrt{p^2 + l^2 + t^2}")
        
        st.markdown("### 🧮 Lab Parameter Digital")
        p = st.number_input("Masukkan Panjang (p):", min_value=1.0, value=6.0, step=1.0)
        l = st.number_input("Masukkan Lebar (l):", min_value=1.0, value=4.0, step=1.0)
        t = st.number_input("Masukkan Tinggi (t):", min_value=1.0, value=3.0, step=1.0)
        
        st.markdown("##### 🔍 Proyeksi Garis Ruang (Interaktif)")
        show_db_balok = st.checkbox("Tampilkan Diagonal Bidang Alas AC")
        show_dr_balok = st.checkbox("Tampilkan Diagonal Ruang AG")
        
        # Perhitungan Metrik Balok
        v_balok = p * l * t
        lp_balok = 2 * ((p * l) + (p * t) + (l * t))
        db_alas = np.sqrt(p**2 + l**2)
        dr_balok = np.sqrt(p**2 + l**2 + t**2)
        
        st.success(f"📊 **Hasil Analisis Struktur Balok:**\n\n"
                   f"🔹 **Volume (V):** {v_balok:.2f} satuan kubik\n\n"
                   f"🔹 **Luas Permukaan (L):** {lp_balok:.2f} satuan persegi\n\n"
                   f"◼️ **Panjang Diagonal Alas AC:** {db_alas:.4f} satuan\n\n"
                   f"🚀 **Panjang Diagonal Ruang AG:** {dr_balok:.4f} satuan")

    with col2:
        st.markdown("### 🌐 Model Proyeksi 3D Interaktif")
        st.caption("Gunakan mouse/kursor untuk memutar (rotate) balok guna menganalisis letak garis.")
        
        x = [0, p, p, 0, 0, p, p, 0]
        y = [0, 0, l, l, 0, 0, l, l]
        z = [0, 0, 0, 0, t, t, t, t]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        
        # Plot Objek 3D Transparan
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.15, color='#198754', flatshading=True, name="Volume"
        ))
        
        # Plot Kerangka Utama (Rusuk)
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#495057', width=3), name="Rusuk"
        ))
        
        # INTERAKSI VISUAL: Diagonal Bidang AC (Balok)
        if show_db_balok:
            fig.add_trace(go.Scatter3d(
                x=[0, p], y=[0, l], z=[0, 0], mode='lines+markers',
                line=dict(color='#dc3545', width=5, dash='dash'),
                marker=dict(size=4), name="Diag. Bidang AC"
            ))
            
        # INTERAKSI VISUAL: Diagonal Ruang AG (Balok)
        if show_dr_balok:
            fig.add_trace(go.Scatter3d(
                x=[0, p], y=[0, l], z=[0, t], mode='lines+markers',
                line=dict(color='#ffc107', width=6),
                marker=dict(size=4), name="Diag. Ruang AG"
            ))
        
        # Label Titik Sudut
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z, mode='markers+text',
            text=labels, textposition="top center",
            marker=dict(size=6, color='black'), name="Titik"
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X (Panjang)', range=[-1, p+2]),
                yaxis=dict(title='Y (Lebar)', range=[-1, l+2]),
                zaxis=dict(title='Z (Tinggi)', range=[-1, t+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("🎨 Aplikasi Lab Geometri / Dimensi Tiga SMK.")
st.sidebar.caption("Pengembang: Mochammad Rifqi Al Khadziq")
