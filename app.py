import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Yuk Belajar Geometri!", 
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DESAIN TAMPILAN CUSTOM (CSS) ---
style_css = """
<style>
    /* Mengubah background utama aplikasi */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4eaf5 100%);
    }
    
    /* Mengunci warna teks agar tidak memutih akibat dark mode */
    .stApp p, .stApp li, .stApp span, .stApp label {
        color: #2E5B88 !important;
    }
    
    /* Mengubah warna teks utama */
    h1 {
        color: #2E5B88 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    h2, h3 {
        color: #4A6FA5 !important;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Desain Kotak Info / Card yang Lucu */
    .kids-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #FF9F43;
        margin-bottom: 20px;
    }
    .kids-card-blue {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #4A90E2;
        margin-bottom: 20px;
    }
</style>
"""
# Menjalankan fungsi markdown dengan parameter underscore (_) yang benar
st.markdown(style_css, unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
sidebar_html = """
<div style='text-align: center;'>
    <h2 style='margin-bottom: 0;'>🎒 Menu Kelas</h2>
    <p style='color: #718096; font-size: 14px;'>Eksplorasi Bangun Ruang</p>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

menu = st.sidebar.selectbox("", ["🏠 Beranda", "🧊 Materi Kubus", "🧱 Materi Balok"])

# --- HALAMAN UTAMA: BERANDA ---
if menu == "🏠 Beranda":
    col_text, col_img = st.columns([3, 2])
    
    with col_text:
        st.title("Petualangan Geometri Interaktif 🤩")
        st.markdown("""
        ### Halo, Teman-Teman Rasa Ingin Tahu! 👋
        Selamat datang di ruang belajar matematika yang seru! Di sini kita akan membedah rahasia di balik benda-benda di sekitar kita yang berbentuk **Kubus** dan **Balok**.
        
        **Apa saja yang bisa kamu lakukan di sini🤔?**
        * 🕵️‍♂️ **Detektif 3D:** Sentuh atau geser bangun ruang dari sudut mana saja sesukamu!
        * 🧮 **Kalkulator Ajaib:** Ketik angka ukurannya, dan simsalabim! Luas dan volumenya langsung terhitung otomatis.
        * 📝 **Catatan Pintar:** Rumus-rumus penting dikemas simpel agar kamu cepat paham.
        
        *Silakan pilih materi **Kubus** atau **Balok** di menu samping kiri untuk mulai bertualang!*
        """)
        
    with col_img:
        st.write("")
        # Ini adalah satu-satunya kode st.image yang kita pakai sekarang (PNG stabil)
        st.image("https://raw.githubusercontent.com/SimatupangRaimon/cdn/main/back-to-school.png", use_container_width=True)
# --- HALAMAN: KUBUS ---
elif menu == "🧊 Materi Kubus":
    st.title("🧊 Ayo Mengenal Si Kotak Sempurna: Kubus")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="kids-card">
            <h3>📋 Sifat Seru Kubus</h3>
            <ul>
                <li>Punya <b>6 sisi</b> berbentuk persegi yang semuanya sama besar (kembar!).</li>
                <li>Punya <b>12 rusuk</b> yang panjangnya sama persis.</li>
                <li>Punya <b>8 titik sudut</b> tempat bertemunya para rusuk.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_kubus, unsafe_allow_html=True)
        
        card_rumus_kubus = """
        <div class="kids-card-blue">
            <h3>📝 Rumus Kilat</h3>
            <p>Ssst.. ini rahasia menghitung kubus dengan cepat:</p>
        </div>
        """
        st.markdown(card_rumus_kubus, unsafe_allow_html=True)
        st.latex(r"Volume \ (V) = s \times s \times s = s^3")
        st.latex(r"Luas \ Permukaan \ (L) = 6 \times s^2")
        
        st.markdown("### 🧮 Lab Eksperimen Angka")
        sisi = st.number_input("Geser atau ketik panjang sisi kubus (s):", min_value=1.0, value=5.0, step=0.5)
        
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        
        st.info(f"💡 **Hasil Eksperimen (Sisi = {sisi}):**\n\n"
                f"🔹 **Volume (V):** {volume:.2f} satuan kubik\n\n"
                f"🔹 **Luas Permukaan (L):** {luas_permukaan:.2f} satuan persegi")

    with col2:
        st.markdown("### 🔍 Teropong 3D Interaktif")
        st.caption("👉 Sentuh atau geser bangun ruang di bawah ini untuk melihatnya dari berbagai sudut!")
        
        s = sisi
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
                opacity=0.7,
                color='#38EF7D',
                flatshading=True,
                name="Kubus"
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X', range=[-1, s+2], backgroundcolor="#f0f0f0"),
                yaxis=dict(title='Y', range=[-1, s+2], backgroundcolor="#f0f0f0"),
                zaxis=dict(title='Z', range=[-1, s+2], backgroundcolor="#f0f0f0")
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN: BALOK ---
elif menu == "🧱 Materi Balok":
    st.title("🧱 Ayo Mengenal Si Kotak Panjang: Balok")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="kids-card">
            <h3>📋 Karakteristik Balok</h3>
            <ul>
                <li>Mirip kubus, tapi sisinya berbentuk persegi panjang.</li>
                <li>Sisi yang <b>berhadapan</b> ukurannya sama besar.</li>
                <li>Punya 3 ukuran utama: <b>Panjang (p), Lebar (l), dan Tinggi (t)</b>.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_balok, unsafe_allow_html=True)
        
        card_rumus_balok = """
        <div class="kids-card-blue">
            <h3>📝 Rumus Kilat</h3>
        </div>
        """
        st.markdown(card_rumus_balok, unsafe_allow_html=True)
        st.latex(r"Volume \ (V) = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L) = 2 \times ((p \times l) + (p \times t) + (l \times t))")
        
        st.markdown("### 🧮 Lab Eksperimen Angka")
        p = st.number_input("Masukkan Panjang (p):", min_value=1.0, value=6.0, step=0.5)
        l = st.number_input("Masukkan Lebar (l):", min_value=1.0, value=4.0, step=0.5)
        t = st.number_input("Masukkan Tinggi (t):", min_value=1.0, value=3.0, step=0.5)
        
        v_balok = p * l * t
        lp_balok = 2 * ((p * l) + (p * t) + (l * t))
        
        st.info(f"💡 **Hasil Eksperimen Balok:**\n\n"
                f"🔹 **Volume (V):** {v_balok:.2f} satuan kubik\n\n"
                f"🔹 **Luas Permukaan (L):** {lp_balok:.2f} satuan persegi")

    with col2:
        st.markdown("### 🔍 Teropong 3D Interaktif")
        st.caption("👉 Sentuh atau geser bangun ruang di bawah ini untuk melihatnya dari berbagai sudut!")
        
        x = [0, p, p, 0, 0, p, p, 0]
        y = [0, 0, l, l, 0, 0, l, l]
        z = [0, 0, 0, 0, t, t, t, t]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
                opacity=0.7,
                color='#FF416C',
                flatshading=True,
                name="Balok"
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Panjang (X)', range=[-1, p+2], backgroundcolor="#f0f0f0"),
                yaxis=dict(title='Lebar (Y)', range=[-1, l+2], backgroundcolor="#f0f0f0"),
                zaxis=dict(title='Tinggi (Z)', range=[-1, t+2], backgroundcolor="#f0f0f0")
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("🎨 Dibuat untuk Media Pembelajaran Matematika SMP.")
st.sidebar.caption("Oleh: Mochammad Rifqi Al Khadziq")
