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
    ["Beranda Analisis", "Analisis Kubus", "Analisis Balok", "Proyeksi Jaring-Jaring"]
)

# --- FUNGSI KERANGKA 3D ---
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
        st.title("Modul Interaktif Bangun Ruang Sisi Datar 🖥️")
        st.markdown("<p style='font-style: italic; color: #6c757d; margin-top: -15px;'>Mata Pelajaran Matematika SMP Kelas 8</p>", unsafe_allow_html=True)
        st.markdown("### Selamat Datang di LabGo 😉")
        st.markdown("Aplikasi pembelajaran interaktif untuk memahami unsur, jaring-jaring, luas permukaan, dan volume kubus serta balok.")
        st.info("👉 Silakan pilih menu di sidebar sebelah kiri untuk mulai mengeksplorasi.")
    with col_img:
        st.write("")
        try:
            st.image("images (4).jpg", use_container_width=True, caption="Media Belajar Matematika SMP")
        except Exception:
            pass
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 13px;'>© 2026 Modul Matematika Kelas 8 SMP | Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)

# --- KUBUS ---
elif pilihan_menu == "Analisis Kubus":
    st.title("🧊 Eksplorasi Kubus (Matematika Kelas 8)")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Kubus</h3>
            <ul>
                <li><b>Sisi:</b> 6 buah persegi yang kongruen.</li>
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
            st.markdown(f"* **Hasil Akhir:** **{volume}** satuan kubik")
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
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

# --- BALOK ---
elif pilihan_menu == "Analisis Balok":
    st.title("🧱 Eksplorasi Balok (Matematika Kelas 8)")
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
            st.markdown(f"* **Hasil Akhir:** **{v_balok}** satuan kubik")
        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan", expanded=True):
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

# --- PROYEKSI JARING-JARING ---
elif pilihan_menu == "Proyeksi Jaring-Jaring":
    st.title("📦 Proyeksi Berbagai Variasi Jaring-Jaring")
    st.markdown("Pilih jenis bangun ruang dan variasi pola jaring-jaring 2 dimensi.")
    
    pilihan_bangun = st.radio("Pilih Bangun Ruang:", ["Jaring-Jaring Kubus (Murni Persegi)", "Jaring-Jaring Balok (Persegi Panjang)"], horizontal=True)
    
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
            st.info("💡 **Variasi 1:** Pola jaring-jaring kubus berbentuk salib dari 6 buah persegi.")
            shapes_list = [
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=2, x1=2, y1=3, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=1, y0=3, x1=2, y1=4, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=0, y0=1, x1=1, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#a3cfbb", opacity=0.8),
            ]
        elif variasi_kubus == "Variasi 2 (Pola Huruf L / Tangga)":
            st.info("💡 **Variasi 2:** Pola jaring-jaring kubus membentuk susunan siku menyerupai huruf L.")
            shapes_list = [
                dict(type="rect", x0=0, y0=0, x1=1, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=1, y0=0, x1=2, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=0, x1=3, y1=1, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=2, y0=2, x1=3, y1=3, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
                dict(type="rect", x0=3, y0=1, x1=4, y1=2, line=dict(color="blue", width=2), fillcolor="#9ec5fe", opacity=0.8),
            ]
        elif variasi_kubus == "Variasi 3 (Pola Zig-Zag Samping)":
            st.info("💡 **Variasi 3:** Pola jaring-jaring kubus dengan posisi menaik bertahap.")
            shapes_list = [
                dict(type="rect", x0=0, y0=2, x1=1, y1=3, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=0, y0=1, x1=1, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=1, y0=1, x1=2, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=2, y0=1, x1=3, y1=2, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=2, y0=0, x1=3, y1=1, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
                dict(type="rect", x0=3, y0=0, x1=4, y1=1, line=dict(color="blue", width=2), fillcolor="#f1aeb5", opacity=0.8),
            ]
        else:
            st.info("💡 **Variasi 4:** Pola jaring-jaring kubus melangkah sejajar.")
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
            st.info("💡 **Variasi 1 Balok:** Jaring-jaring balok dengan sisi panjang dan pendek yang bersesuaian.")
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
            st.info("💡 **Variasi 2 Balok (T-Shape):** Pola jaring-jaring alternatif balok yang membentuk T.")
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
