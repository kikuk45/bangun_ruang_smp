import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Konfigurasi Halaman
st.set_page_config(
    page_title="Media Pembelajaran Interaktif 3D - Dimensi Tiga",
    page_icon="📐",
    layout="wide"
)

# Judul Utama
st.title("📐 Media Pembelajaran Interaktif 3D: Bangun Ruang Sisi Datar")
st.markdown("Eksplorasi rumus, jaring-jaring, dan visualisasi 3D untuk membantu pemahaman konsep dimensi tiga secara interaktif.")

# Menu Navigasi Sederhana
menu = st.sidebar.selectbox(
    "Pilih Menu Bangun Ruang:",
    ["Kubus", "Balok", "Prisma Segitiga", "Limas Segitiga", "Limas Segiempat"]
)

# ----------------------------------------------------
# 1. KUBUS
# ----------------------------------------------------
if menu == "Kubus":
    st.header("🧊 Eksplorasi Kubus")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Rumus Kubus")
        st.latex(r"Volume (V) = s^3")
        st.latex(r"Luas Permukaan (L_p) = 6 \times s^2")
        st.latex(r"Panjang Diagonal Ruang = s \sqrt{3}")
        
        sisi = st.slider("Panjang Rusuk (s):", min_value=1.0, max_value=10.0, value=4.0, step=0.5)
        
        v = sisi ** 3
        lp = 6 * (sisi ** 2)
        diag = round(sisi * np.sqrt(3), 2)
        
        st.info(f"**Volume:** {v}")
        st.info(f"**Luas Permukaan:** {lp}")
        st.info(f"**Diagonal Ruang:** {diag}")
        
    with col2:
        st.markdown("### 🌐 Visualisasi 3D Kubus")
        
        # Koordinat titik kubus
        x_pts = [0, sisi, sisi, 0, 0, sisi, sisi, 0]
        y_pts = [0, 0, sisi, sisi, 0, 0, sisi, sisi]
        z_pts = [0, 0, 0, 0, sisi, sisi, sisi, sisi]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x_pts, y=y_pts, z=z_pts,
                i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 2, 7],
                color='#ffc107', opacity=0.3, flatshading=True
            ),
            go.Scatter3d(
                x=[0, sisi, sisi, 0, 0, 0, sisi, sisi, sisi, 0, 0, sisi, sisi, 0, 0, sisi],
                y=[0, 0, sisi, sisi, 0, 0, 0, sisi, sisi, sisi, 0, 0, sisi, sisi, sisi, sisi],
                z=[0, 0, 0, 0, 0, sisi, sisi, sisi, 0, 0, sisi, sisi, sisi, sisi, 0, 0],
                mode='lines',
                line=dict(color='black', width=4)
            )
        ])
        fig.update_layout(scene=dict(xaxis=dict(range=[-1, 11]), yaxis=dict(range=[-1, 11]), zaxis=dict(range=[-1, 11])))
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# 2. BALOK
# ----------------------------------------------------
elif menu == "Balok":
    st.header("📦 Eksplorasi Balok")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Rumus Balok")
        st.latex(r"Volume (V) = p \times l \times t")
        st.latex(r"Luas Permukaan (L_p) = 2 \times (p \cdot l + p \cdot t + l \cdot t)")
        
        p = st.number_input("Panjang (p):", min_value=1.0, max_value=10.0, value=5.0)
        l = st.number_input("Lebar (l):", min_value=1.0, max_value=10.0, value=3.0)
        t = st.number_input("Tinggi (t):", min_value=1.0, max_value=10.0, value=4.0)
        
        v = p * l * t
        lp = 2 * (p*l + p*t + l*t)
        
        st.info(f"**Volume:** {v}")
        st.info(f"**Luas Permukaan:** {lp}")
        
    with col2:
        st.markdown("### 🌐 Visualisasi 3D Balok")
        
        x_pts = [0, p, p, 0, 0, p, p, 0]
        y_pts = [0, 0, l, l, 0, 0, l, l]
        z_pts = [0, 0, 0, 0, t, t, t, t]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x_pts, y=y_pts, z=z_pts,
                i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 2, 7],
                color='#17a2b8', opacity=0.3, flatshading=True
            ),
            go.Scatter3d(
                x=[0, p, p, 0, 0, 0, p, p, p, 0, 0, p, p, 0, 0, p],
                y=[0, 0, l, l, 0, 0, 0, l, l, l, 0, 0, l, l, l, l],
                z=[0, 0, 0, 0, 0, t, t, t, t, 0, 0, t, t, t, 0, 0],
                mode='lines',
                line=dict(color='black', width=4)
            )
        ])
        fig.update_layout(scene=dict(xaxis=dict(range=[-1, 11]), yaxis=dict(range=[-1, 11]), zaxis=dict(range=[-1, 11])))
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# 3. PRISMA SEGITIGA (Dengan Titik Sudut/Label)
# ----------------------------------------------------
elif menu == "Prisma Segitiga":
    st.header("⛺ Eksplorasi Prisma Segitiga")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Rumus Prisma Segitiga")
        st.latex(r"Volume (V) = \text{Luas Alas} \times \text{Tinggi Prisma}")
        st.latex(r"Luas Permukaan (L_p) = (2 \times \text{Luas Alas}) + (\text{Keliling Alas} \times \text{Tinggi Prisma})")
        
        AB = st.number_input("Panjang Sisi Alas AB:", min_value=1.0, max_value=10.0, value=4.0)
        BC = st.number_input("Panjang Sisi Alas BC:", min_value=1.0, max_value=10.0, value=3.0)
        tinggi_tri = st.number_input("Tinggi Alas Segitiga (t_alas):", min_value=1.0, max_value=10.0, value=3.0)
        tinggi_pris = st.number_input("Tinggi Prisma (AD/BE/CF):", min_value=1.0, max_value=10.0, value=6.0)
        
        luas_alas = 0.5 * AB * tinggi_tri
        keliling_alas = AB + BC + BC  # Asumsi segitiga sama kaki / umum sederhana
        v = luas_alas * tinggi_pris
        lp = (2 * luas_alas) + (keliling_alas * tinggi_pris)
        
        st.info(f"**Luas Alas:** {luas_alas}")
        st.info(f"**Volume Prisma:** {v}")
        st.info(f"**Luas Permukaan Prisma:** {lp}")
        
    with col2:
        st.markdown("### 🌐 Visualisasi 3D Prisma Segitiga (Sesuai Orientasi Foto)")
        
        xa, ya, za = 0.0, 0.0, 0.0                      # A
        xb, yb, zb = float(AB), 0.0, 0.0                # B
        xc, yc, zc = float(AB)/2, float(tinggi_tri), 0.0  # C
        
        xd, yd, zd = 0.0, 0.0, float(tinggi_pris)                     # D
        xe, ye, ze = float(AB), 0.0, float(tinggi_pris)               # E
        xf, yf, zf = float(AB)/2, float(tinggi_tri), float(tinggi_pris) # F
        
        x_pts = [xa, xb, xc, xd, xe, xf]
        y_pts = [ya, yb, yc, yd, ye, yf]
        z_pts = [za, zb, zc, zd, ze, zf]
        
        fig = go.Figure(data=[
            # Gambar bangun ruang (mesh)
            go.Mesh3d(
                x=x_pts, y=y_pts, z=z_pts,
                i=[0, 0, 0, 3, 3],
                j=[1, 2, 3, 4, 5],
                k=[2, 3, 4, 5, 4],
                color='#ffc107', opacity=0.3, flatshading=True
            ),
            # Garis kerangka tepi
            go.Scatter3d(
                x=[xa, xb, xc, xa, xd, xe, xf, xd, xa, xd, xb, xe, xc, xf],
                y=[ya, yb, yc, ya, yd, ye, yf, yd, ya, yd, yb, ye, yc, yf],
                z=[za, zb, zc, za, zd, ze, zf, zd, za, zd, zb, ze, zc, zf],
                mode='lines',
                line=dict(color='black', width=4)
            ),
            # Titik sudut dan label teks (A, B, C, D, E, F)
            go.Scatter3d(
                x=x_pts, y=y_pts, z=z_pts,
                mode='text+markers',
                text=[' A', ' B', ' C', ' D', ' E', ' F'],
                textposition='top center',
                marker=dict(size=6, color='red')
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(range=[-1, AB+2], title='X'),
                yaxis=dict(range=[-1, tinggi_tri+2], title='Y'),
                zaxis=dict(range=[-1, tinggi_pris+2], title='Z')
            ), 
            margin=dict(l=0, r=0, b=0, t=0)
        )
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# 4. LIMAS SEGITIGA
# ----------------------------------------------------
elif menu == "Limas Segitiga":
    st.header(" пирамида / Eksplorasi Limas Segitiga")
    st.info("Fitur Limas Segitiga sedang dalam pengembangan modul interaktif.")

# ----------------------------------------------------
# 5. LIMAS SEGIEMPAT
# ----------------------------------------------------
elif menu == "Limas Segiempat":
    st.header("🔺 Eksplorasi Limas Segiempat")
    st.info("Fitur Limas Segiempat sedang dalam pengembangan modul interaktif.")
