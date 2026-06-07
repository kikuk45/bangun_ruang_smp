import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Media Pembelajaran Geometri SMP", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HEADER APLIKASI ---
st.title("📐 Media Pembelajaran Geometri Interaktif")
st.subheader("Materi: Bangun Ruang Sisi Datar (SMP)")
st.write("Selamat belajar! Pilih bangun ruang di menu samping untuk mulai mengeksplorasi.")

# --- SIDEBAR NAVIGASI ---
st.sidebar.header("Menu Pembelajaran")
menu = st.sidebar.selectbox("Pilih Halaman:", ["Home", "Kubus", "Balok"])

# --- HALAMAN UTAMA (HOME) ---
if menu == "Home":
    st.markdown("""
    ### Halo, Selamat Datang! 👋
    Aplikasi ini dirancang khusus untuk membantu kamu memahami konsep **Bangun Ruang Sisi Datar** dengan lebih mudah, visual, dan interaktif.
    
    **Fitur yang bisa kamu coba di aplikasi ini:**
    * 🧊 **Visualisasi 3D:** Kamu bisa memutar, memperbesar, dan melihat bentuk bangun ruang dari berbagai sudut secara langsung.
    * 🧮 **Kalkulator Pintar:** Masukkan angka dimensinya, dan aplikasi akan menghitung Luas Permukaan serta Volume secara instan.
    * 📝 **Rumus Matematika:** Dilengkapi dengan rumus standar yang mudah dipahami.
    
    *Silakan pilih materi **Kubus** atau **Balok** pada menu di samping kiri untuk memulai petualangan belajarmu!*
    """)

# --- HALAMAN KUBUS ---
elif menu == "Kubus":
    st.header("🧊 Bangun Ruang: Kubus")
    
    # Membagi halaman menjadi 2 kolom (Kiri untuk teori/input, Kanan untuk visualisasi 3D)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📋 Sifat & Karakteristik Kubus")
        st.write("- Memiliki **6 sisi** berbentuk persegi yang kongruen (sama besar).")
        st.write("- Memiliki **12 rusuk** yang sama panjang.")
        st.write("- Memiliki **8 titik sudut**.")
        
        st.markdown("### 📝 Rumus Dasar")
        st.latex(r"Volume \ (V) = s \times s \times s = s^3")
        st.latex(r"Luas \ Permukaan \ (L) = 6 \times s^2")
        
        st.markdown("### 🧮 Mari Mencoba (Kalkulator Interaktif)")
        # Input Panjang Sisi (Siswa bisa mengubah nilai ini)
        sisi = st.number_input("Masukkan panjang sisi kubus (s):", min_value=1.0, value=5.0, step=0.5)
        
        # Proses Perhitungan matematika
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        
        # Menampilkan Hasil
        st.success(f"**Hasil Perhitungan untuk Kubus dengan sisi = {sisi}:**")
        st.write(f"🔹 **Volume (V):** {volume:.2f} satuan kubik")
        st.write(f"🔹 **Luas Permukaan (L):** {luas_permukaan:.2f} satuan persegi")

    with col2:
        st.markdown("### 🔍 Visualisasi 3D Interaktif")
        st.caption("Sentuh/Klik pada gambar lalu geser untuk memutar objek kubus")
        
        # Membuat titik koordinat 3D Kubus berdasarkan input sisi
        s = sisi
        x = [0, s, s, 0, 0, s, s, 0]
        y = [0, 0, s, s, 0, 0, s, s]
        z = [0, 0, 0, 0, s, s, s, s]
        
        # Membuat jaring-jaring objek 3D menggunakan Plotly Mesh3d
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
                opacity=0.6,
                color='skyblue',
                flatshading=True,
                name="Kubus"
            )
        ])
        
        # Mengatur tampilan layout kubus
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Sumbu X', range=[-1, s+2]),
                yaxis=dict(title='Sumbu Y', range=[-1, s+2]),
                zaxis=dict(title='Sumbu Z', range=[-1, s+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN BALOK ---
elif menu == "Balok":
    st.header("🧱 Bangun Ruang: Balok")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📋 Sifat & Karakteristik Balok")
        st.write("- Memiliki **6 sisi**, di mana sisi yang berhadapan sejajar dan sama besar.")
        st.write("- Memiliki **12 rusuk** (terdiri dari 4 kelompok panjang, 4 lebar, dan 4 tinggi).")
        st.write("- Memiliki **8 titik sudut**.")
        
        st.markdown("### 📝 Rumus Dasar")
        st.latex(r"Volume \ (V) = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L) = 2 \times ((p \times l) + (p \times t) + (l \times t))")
        
        st.markdown("### 🧮 Mari Mencoba (Kalkulator Interaktif)")
        # Input Dimensi Balok (Panjang, Lebar, Tinggi)
        p = st.number_input("Masukkan Panjang (p):", min_value=1.0, value=6.0, step=0.5)
        l = st.number_input("Masukkan Lebar (l):", min_value=1.0, value=4.0, step=0.5)
        t = st.number_input("Masukkan Tinggi (t):", min_value=1.0, value=3.0, step=0.5)
        
        # Proses Perhitungan matematika
        v_balok = p * l * t
        lp_balok = 2 * ((p * l) + (p * t) + (l * t))
        
        # Menampilkan Hasil
        st.success("**Hasil Perhitungan untuk Balok:**")
        st.write(f"🔹 **Volume (V):** {v_balok:.2f} satuan kubik")
        st.write(f"🔹 **Luas Permukaan (L):** {lp_balok:.2f} satuan persegi")

    with col2:
        st.markdown("### 🔍 Visualisasi 3D Interaktif")
        st.caption("Sentuh/Klik pada gambar lalu geser untuk memutar objek balok")
        
        # Membuat titik koordinat 3D Balok berdasarkan input p, l, t
        x = [0, p, p, 0, 0, p, p, 0]
        y = [0, 0, l, l, 0, 0, l, l]
        z = [0, 0, 0, 0, t, t, t, t]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
                opacity=0.6,
                color='lightgreen',
                flatshading=True,
                name="Balok"
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Sumbu X', range=[-1, p+2]),
                yaxis=dict(title='Sumbu Y', range=[-1, l+2]),
                zaxis=dict(title='Sumbu Z', range=[-1, t+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("Media Pembelajaran Matematika Geometri SMP v1.0")
