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

pilihan_menu = st.sidebar.selectbox("Pilih Menu Pembelajaran:", ["Beranda Analisis", "Analisis Kubus", "Analisis Balok"])

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
        st.markdown("* 🧮 **Perhitungan Bertahap:** Mempelajari rumus Volume dan Luas Permukaan secara runtut (langkah demi langkah dari substitusi angka hingga hasil akhir berbentuk bilangan bulat).")
        st.markdown("* 🌐 **Visualisasi 3D Interaktif:** Membantu siswa membayangkan bentuk nyata kubus dan balok dari berbagai sudut.")
        st.write("")
        st.info("👉 Silakan pilih menu di sidebar sebelah kiri untuk mulai mengeksplorasi Kubus atau Balok.")
        
    with col_img:
        st.write("")
        try:
            st.image("images (4).jpg", use_container_width=True, caption="Media Belajar Matematika SMP")
        except Exception:
            st.info("💡 **Tips Guru/Siswa:** Gunakan rincian langkah pengerjaan di bawah kalkulator untuk menuliskan catatan di buku catatan matematika.")
            
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 13px;'>© 2026 Modul Matematika Kelas 8 SMP | Dibuat oleh Mochammad Rifqi Al Khadziq</p>", unsafe_allow_html=True)

# --- HALAMAN: KUBUS KELAS 8 ---
elif pilihan_menu == "Analisis Kubus Kelas 8":
    st.title("🧊 Eksplorasi Kubus (Matematika Kelas 8)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_kubus = """
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Kubus (Kelas 8)</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 6 sisi berbentuk persegi yang kongruen (sama besar). Contoh: Sisi ABCD, EFGH, ABFE, dsb.</li>
                <li><b>Rusuk:</b> Memiliki 12 rusuk yang sama panjang (dilambangkan dengan huruf <i>s</i>).</li>
                <li><b>Titik Sudut:</b> Memiliki 8 titik sudut (A, B, C, D, E, F, G, H).</li>
                <li><b>Diagonal Sisi/Bidang:</b> Memiliki 12 garis diagonal pada sisi-sisinya.</li>
                <li><b>Jaring-jaring:</b> Terdiri dari 6 buah persegi yang saling terhubung jika dibuka.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_kubus, unsafe_allow_html=True)
        
        card_rumus_kubus = """
        <div class="smp-card-tech">
            <h3>📝 Rumus Utama Kubus Kelas 8</h3>
        </div>
        """
        st.markdown(card_rumus_kubus, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = sisi \times sisi \times sisi \ (s^3)")
        st.latex(r"Luas \ Permukaan \ (L_p) = 6 \times (sisi \times sisi)")
        
        st.markdown("### 🧮 Kalkulator & Langkah Pengerjaan Kubus")
        sisi = st.number_input("Masukkan Panjang Sisi Kubus (s):", min_value=1, value=5, step=1, format="%d")
        
        # Perhitungan Metrik Kubus (Bilangan Bulat)
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        
        # Penjabaran Langkah demi Langkah untuk Kelas 8
        st.markdown("### 📋 Rincian Langkah Pengerjaan (Step-by-Step):")
        
        with st.expander("1️⃣ Langkah Menghitung Volume Kubus", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Volume adalah kapasitas ruang yang dapat diisi oleh kubus.")
            st.markdown(r"* **Rumus:** $V = s \times s \times s$")
            st.markdown(f"* **Langkah Substitusi:** Masukkan nilai panjang sisi $s = {sisi}$, sehingga $V = {sisi} \\times {sisi} \\times {sisi}$")
            st.markdown(f"* **Proses Perkalian:** $({sisi} \\times {sisi}) = {sisi*sisi}$, lalu dikali {sisi} lagi.")
            st.markdown(f"* **Hasil Akhir:** **{volume}** satuan kubik")

        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Kubus", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Luas permukaan adalah total luas dari 6 buah sisi persegi yang menyelimuti kubus.")
            st.markdown(r"* **Rumus:** $L_p = 6 \times (s \times s)$")
            st.markdown(f"* **Langkah Substitusi:** $L_p = 6 \\times ({sisi} \\times {sisi})$")
            st.markdown(f"* **Proses Hitung Sisi Persegi:** Luas satu sisi = ${sisi} \\times {sisi} = {sisi**2}$")
            st.markdown(f"* **Proses Perkalian Akhir:** $6 \\times {sisi**2}$")
            st.markdown(f"* **Hasil Akhir:** **{luas_permukaan}** satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Kubus")
        st.caption("Putar kursor pada objek untuk melihat bentuk ruang kubus secara nyata.")
        
        s = float(sisi)
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
            opacity=0.20, color='#0d6efd', flatshading=True, name="Ruang Kubus"
        ))
        
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#343a40', width=4), name="Rusuk Kubus"
        ))
        
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z, mode='markers+text',
            text=labels, textposition="top center",
            marker=dict(size=6, color='black'), name="Titik Sudut"
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Sumbu X', range=[-1, s+2]),
                yaxis=dict(title='Sumbu Y', range=[-1, s+2]),
                zaxis=dict(title='Sumbu Z', range=[-1, s+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN: BALOK KELAS 8 ---
elif pilihan_menu == "Analisis Balok Kelas 8":
    st.title("🧱 Eksplorasi Balok (Matematika Kelas 8)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="smp-card">
            <h3>📋 Karakteristik & Unsur Balok (Kelas 8)</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 6 sisi berbentuk persegi panjang, dengan 3 pasang sisi berhadapan yang sejajar dan sama luas (Depan-Belakang, Atas-Bawah, Kiri-Kanan).</li>
                <li><b>Rusuk:</b> Memiliki 12 rusuk yang dikelompokkan menjadi 3 ukuran: Panjang (<i>p</i>), Lebar (<i>l</i>), dan Tinggi (<i>t</i>).</li>
                <li><b>Titik Sudut:</b> Memiliki 8 titik sudut (A, B, C, D, E, F, G, H).</li>
                <li><b>Jaring-jaring:</b> Rangkaian 6 persegi panjang yang dapat membentuk balok jika dilipat.</li>
            </ul>
        </div>
        """
        st.markdown(card_sifat_balok, unsafe_allow_html=True)
        
        card_rumus_balok = """
        <div class="smp-card-tech">
            <h3>📝 Rumus Utama Balok Kelas 8</h3>
        </div>
        """
        st.markdown(card_rumus_balok, unsafe_allow_html=True)
        
        st.latex(r"Volume \ (V) = p \times l \times t")
        st.latex(r"Luas \ Permukaan \ (L_p) = 2 \times (p \cdot l + p \cdot t + l \cdot t)")
        
        st.markdown("### 🧮 Kalkulator & Langkah Pengerjaan Balok")
        p = st.number_input("Masukkan Panjang (p):", min_value=1, value=6, step=1, format="%d")
        l = st.number_input("Masukkan Lebar (l):", min_value=1, value=4, step=1, format="%d")
        t = st.number_input("Masukkan Tinggi (t):", min_value=1, value=3, step=1, format="%d")
        
        # Perhitungan Metrik Balok (Bilangan Bulat)
        v_balok = p * l * t
        pl = p * l
        pt = p * t
        lt = l * t
        lp_balok = 2 * (pl + pt + lt)
        
        # Penjabaran Langkah demi Langkah untuk Kelas 8
        st.markdown("### 📋 Rincian Langkah Pengerjaan (Step-by-Step):")
        
        with st.expander("1️⃣ Langkah Menghitung Volume Balok", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Volume dihitung dengan mengalikan luas alas dengan tinggi balok ($V = \text{Luas Alas} \times t$).")
            st.markdown(r"* **Rumus:** $V = p \times l \times t$")
            st.markdown(f"* **Langkah Substitusi:** $V = {p} \\times {l} \\times {t}$")
            st.markdown(f"* **Proses Hitung Tahap 1:** Hitung perkalian panjang dan lebar dahulu: $({p} \\times {l}) = {p*l}$")
            st.markdown(f"* **Proses Hitung Tahap 2:** Kalikan hasilnya dengan tinggi: ${p*l} \\times {t}$")
            st.markdown(f"* **Hasil Akhir:** **{v_balok}** satuan kubik")

        with st.expander("2️⃣ Langkah Menghitung Luas Permukaan Balok", expanded=True):
            st.markdown(r"* **Konsep Dasar:** Luas permukaan adalah jumlah dari luas seluruh 3 pasang sisi yang saling berhadapan.")
            st.markdown(r"* **Rumus:** $L_p = 2 \times (p\cdot l + p\cdot t + l\cdot t)$")
            st.markdown(r"* **Langkah 1 (Hitung Luas Tiap Pasang Sisi):**")
            st.markdown(f"  * Luas Sisi Alas & Atas $(p \\times l) = {p} \\times {l} = {pl}$")
            st.markdown(f"  * Luas Sisi Depan & Belakang $(p \\times t) = {p} \\times {t} = {pt}$")
            st.markdown(f"  * Luas Sisi Samping Kiri & Kanan $(l \\times t) = {l} \\times {t} = {lt}$")
            st.markdown(f"* **Langkah 2 (Jumlahkan Ketiganya):** $({pl} + {pt} + {lt}) = {pl + pt + lt}$")
            st.markdown(f"* **Langkah 3 (Kalikan dengan 2):** $2 \\times {pl + pt + lt}$")
            st.markdown(f"* **Hasil Akhir:** **{lp_balok}** satuan persegi")

    with col2:
        st.markdown("### 🌐 Visualisasi 3D Balok")
        st.caption("Putar kursor pada objek untuk melihat bentuk ruang balok secara nyata.")
        
        pf, lf, tf = float(p), float(l), float(t)
        x = [0, pf, pf, 0, 0, pf, pf, 0]
        y = [0, 0, lf, lf, 0, 0, lf, lf]
        z = [0, 0, 0, 0, tf, tf, tf, tf]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        fig = go.Figure()
        
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.20, color='#198754', flatshading=True, name="Ruang Balok"
        ))
        
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, z=zl, mode='lines',
            line=dict(color='#343a40', width=4), name="Rusuk Balok"
        ))
        
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z, mode='markers+text',
            text=labels, textposition="top center",
            marker=dict(size=6, color='black'), name="Titik Sudut"
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='Sumbu X (Panjang)', range=[-1, pf+2]),
                yaxis=dict(title='Sumbu Y (Lebar)', range=[-1, lf+2]),
                zaxis=dict(title='Sumbu Z (Tinggi)', range=[-1, tf+2])
            ),
            margin=dict(l=0, r=0, b=0, t=0), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

# --- FOOTER SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.caption("Pengembang: Mochammad Rifqi Al Khadziq")
