import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Modul Bangun Ruang SMP", 
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
    <p style='color: #6c757d; font-size: 14px;'>Media Pembelajaran Matematika SMP</p>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

pilihan_menu = st.sidebar.selectbox("", ["Beranda Analisis", "Analisis Kubus", "Analisis Balok"])

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
        st.title("Aplikasi Bangun Ruang Sisi Datar 🖥️")
        st.markdown("<p style='font-style: italic; color: #6c757d; margin-top: -15px;'>Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)
        
        st.markdown("### Selamat Datang di Modul Geometri Ruang SMP!")
        st.markdown("Aplikasi interaktif ini dirancang untuk membantu memahami unsur-unsur, luas permukaan, dan volume bangun ruang sisi datar disertai **tahapan perhitungan langkah demi langkah**.")
        
        st.markdown("**Fitur Utama Laboratorium Virtual:**")
        st.markdown("* 🌐 **Visualisasi Objek 3D Dinamis:** Memutar sudut pandang bangun ruang secara interaktif.")
        st.markdown("* 📝 **Penjabaran Langkah Kerja:** Membimbing siswa memahami rumus dari proses substitusi nilai hingga hasil akhir.")
        st.markdown("* 🔍 **Eksplorasi Diagonal (Pengayaan):** Mengenal garis diagonal bidang dan ruang.")
        st.write("")
        st.info("Silakan pilih menu objek di sebelah kiri untuk memulai pembelajaran.")
        
    with col_img:
        st.write("")
        try:
            st.image("images (4).jpg", use_container_width=True, caption="Media Pembelajaran Bangun Ruang")
        except Exception:
            st.info("💡 **Tips Belajar SMP:** Perhatikan rincian langkah pengerjaan agar lebih mudah memahami penurunan rumus matematika.")
            
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 13px;'>© 2026 Modul Bangun Ruang SMP | Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)

# --- HALAMAN: KUBUS ---
elif pilihan_menu == "Analisis Kubus":
    st.title("🧊 Eksplorasi Bangun Ruang: Kubus")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="smp-card">
            <h3>📋 Unsur-Unsur Kubus</h3>
            <ul>
                <li><b>6 Sisi (Bidang):</b> Berbentuk persegi yang kongruen.</li>
                <li><b>12 Rusuk:</b> Memiliki panjang yang sama besar (<i>s</i>).</li>
                <li><b>8 Titik Sudut:</b> Pojok-pojok pertemuan antar rusuk.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_kubus, unsafe_allow_html=True)
        
        card_rumus_kubus = """
        <div class="smp-card-tech">
            <h3>📝 Rumus Dasar Kubus</h3>
        </div>
        """
        st.markdown(card_rumus_kubus, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = s^3")
        st.latex(r"Luas \ Permukaan \ (L_p) = 6 \times s^2")
        
        st.markdown("### 🧮 Kalkulator & Langkah Pengerjaan Kubus")
        sisi = st.number_input("Masukkan Panjang Sisi Kubus (s):", min_value=1.0, value=5.0, step=1.0)
        
        st.markdown("##### 🔍 Pengayaan Garis Ruang")
        show_db = st.checkbox("Tampilkan Diagonal Bidang AC (Alas)")
        show_dr = st.checkbox("Tampilkan Diagonal Ruang AG")
        
        # Perhitungan Metrik internal
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        diag_bidang = sisi * np.sqrt(2)
        diag_ruang = sisi * np.sqrt(3)
        
        # Penjabaran Langkah demi Langkah untuk Kubus
        st.markdown("### 📋 Rincian Langkah Perhitungan:")
        
        with st.expander("1️⃣ Langkah Perhitungan Volume (V)", expanded=True):
            st.markdown(f"* **Rumus:** $V = s \\times s \\times s$")
            st.markdown(f"* **Substitusi Nilai:** $V = {sisi} \\times {sisi} \\times {sisi}$")
            st.markdown(f"* **Hasil Akhir:** **{volume:.2f}** satuan kubik")

        with st.expander("2️⃣ Langkah Perhitungan Luas Permukaan ($L_p$)", expanded=True):
            st.markdown(f"* **Rumus:** $L_p = 6 \\times s^2$")
            st.markdown(f"* **Substitusi Nilai:** $L_p = 6 \\times ({sisi} \\times {sisi})$")
            st.markdown(f"* **Proses:** $L_p = 6 \\times {sisi**2}$")
            st.markdown(f"* **Hasil Akhir:** **{luas_permukaan:.2f}** satuan persegi")

        with st.expander("3️⃣ Langkah Perhitungan Diagonal Bidang (AC)", expanded=False):
            st.markdown(f"* **Rumus:** $D_b = s\\sqrt{{2}}$")
            st.markdown(f"* **Substitusi Nilai:** $D_b = {sisi}\\sqrt{{2}}$")
            st.markdown(f"* **Hasil Akhir:** **{diag_bidang:.2f}** satuan")

        with st.expander("4️⃣ Langkah Perhitungan Diagonal Ruang (AG)", expanded=False):
            st.markdown(f"* **Rumus:** $D_r = s\\sqrt{{3}}$")
            st.markdown(f"* **Substitusi Nilai:** $D_r = {sisi}\\sqrt{{3}}$")
            st.markdown(f"* **Hasil Akhir:** **{diag_ruang:.2f}** satuan")

    with col2:
        st.markdown("### 🌐 Model Visualisasi 3D")
        st.caption("Gunakan kursor untuk memutar (rotate) kubus.")
        
        s = sisi
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.15, color='#0d6efd', flatshading=True, name="Volume"
        ))
        
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#495057', width=3), name="Rusuk"
        ))
        
        if show_db:
            fig.add_trace(go.Scatter3d(
                x=[0, s], y=[0, s], z=[0, 0], mode='lines+markers',
                line=dict(color='#dc3545', width=5, dash='dash'),
                marker=dict(size=4), name="Diag. Bidang AC"
            ))
            
        if show_dr:
            fig.add_trace(go.Scatter3d(
                x=[0, s], y=[0, s], z=[0, s], mode='lines+markers',
                line=dict(color='#ffc107', width=6),
                marker=dict(size=4), name="Diag. Ruang AG"
            ))
        
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
elif pilihan_menu == "Analisis Balok":
    st.title("🧱 Eksplorasi Bangun Ruang: Balok")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="smp-card">
            <h3>📋 Unsur-Unsur Balok</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 3 pasang bidang berhadapan sejajar dan sama luas.</li>
                <li><b>Dimensi:</b> Panjang (<i>p</i>), Lebar (<i>l</i>), dan Tinggi (<i>t</i>).</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_balok, unsafe_allow_html=True)
        
        card_rumus_balok = """
        <div class="smp-card-tech">
            <h3>📝 Rumus Dasar Balok</h3>
        </div>
        """
        st.markdown(card_rumus_balok, unsafe_allow_html=True)
        
        st.latex(r"Volume = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L_p) = 2 \times (pl + pt + lt)")
        
        st.markdown("### 🧮 Kalkulator & Langkah Pengerjaan Balok")
        p = st.number_input("Masukkan Panjang (p):", min_value=1.0, value=6.0, step=1.0)
        l = st.number_input("Masukkan Lebar (l):", min_value=1.0, value=4.0, step=1.0)
        t = st.number_input("Masukkan Tinggi (t):", min_value=1.0, value=3.0, step=1.0)
        
        st.markdown("##### 🔍 Pengayaan Garis Ruang")
        show_db_balok = st.checkbox("Tampilkan Diagonal Bidang Alas AC")
        show_dr_balok = st.checkbox("Tampilkan Diagonal Ruang AG")
        
        # Perhitungan Metrik Balok internal
        v_balok = p * l * t
        pl = p * l
        pt = p * t
        lt = l * t
        lp_balok = 2 * (pl + pt + lt)
        db_alas = np.sqrt(p**2 + l**2)
        dr_balok = np.sqrt(p**2 + l**2 + t**2)
        
        # Penjabaran Langkah demi Langkah untuk Balok
        st.markdown("### 📋 Rincian Langkah Perhitungan:")
        
        with st.expander("1️⃣ Langkah Perhitungan Volume (V)", expanded=True):
            st.markdown(f"* **Rumus:** $V = p \\times l \\times t$")
            st.markdown(f"* **Substitusi Nilai:** $V = {p} \\times {l} \\times {t}$")
            st.markdown(f"* **Hasil Akhir:** **{v_balok:.2f}** satuan kubik")

        with st.expander("2️⃣ Langkah Perhitungan Luas Permukaan ($L_p$)", expanded=True):
            st.markdown(f"* **Rumus:** $L_p = 2 \\times (p\\cdot l + p\\cdot t + l\\cdot t)$")
            st.markdown(f"* **Hitung Luas Sisi:**")
            st.markdown(f"  * $(p \\times l) = {p} \\times {l} = {pl}$")
            st.markdown(f"  * $(p \\times t) = {p} \\times {t} = {pt}$")
            st.markdown(f"  * $(l \\times t) = {l} \\times {t} = {lt}$")
            st.markdown(f"* **Jumlahkan:** $({pl} + {pt} + {lt}) = {pl + pt + lt}$")
            st.markdown(f"* **Kalikan 2:** $2 \\times {pl + pt + lt} =$ **{lp_balok:.2f}** satuan persegi")

        with st.expander("3️⃣ Langkah Perhitungan Diagonal Alas (AC)", expanded=False):
            st.markdown(f"* **Rumus:** $AC = \\sqrt{{p^2 + l^2}}$")
            st.markdown(f"* **Substitusi:** $AC = \\sqrt{{{p}^2 + {l}^2}} = \\sqrt{{{p**2} + {l**2}}} = \\sqrt{{{p**2 + l**2}}}$")
            st.markdown(f"* **Hasil Akhir:** **{db_alas:.2f}** satuan")

        with st.expander("4️⃣ Langkah Perhitungan Diagonal Ruang (AG)", expanded=False):
            st.markdown(f"* **Rumus:** $AG = \\sqrt{{p^2 + l^2 + t^2}}$")
            st.markdown(f"* **Substitusi:** $AG = \\sqrt{{{p}^2 + {l}^2 + {t}^2}} = \\sqrt{{{p**2} + {l**2} + {t**2}}}$")
            st.markdown(f"* **Hasil Akhir:** **{dr_balok:.2f}** satuan")

    with col2:
        st.markdown("### 🌐 Model Visualisasi 3D")
        st.caption("Gunakan kursor untuk memutar (rotate) balok.")
        
        x = [0, p, p, 0, 0, p, p, 0]
        y = [0, 0, l, l, 0, 0, l, l]
        z = [0, 0, 0, 0, t, t, t, t]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.15, color='#198754', flatshading=True, name="Volume"
        ))
        
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#495057', width=3), name="Rusuk"
        ))
        
        if show_db_balok:
            fig.add_trace(go.Scatter3d(
                x=[0, p], y=[0, l], z=[0, 0], mode='lines+markers',
                line=dict(color='#dc3545', width=5, dash='dash'),
                marker=dict(size=4), name="Diag. Bidang AC"
            ))
            
        if show_dr_balok:
            fig.add_trace(go.Scatter3d(
                x=[0, p], y=[0, l], z=[0, t], mode='lines+markers',
                line=dict(color='#ffc107', width=6),
                marker=dict(size=4), name="Diag. Ruang AG"
            ))
        
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

# --- FOOTER SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.caption("Pengembang: Mochammad Rifqi Al Khadziq")
