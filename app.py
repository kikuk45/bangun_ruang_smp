# --- HALAMAN: BALOK ---
elif menu == "🧱 Analisis Balok":
    st.title("🧱 Analisis Geometri Ruang: Balok (Prisma Tegak Segiempat)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        card_sifat_balok = """
        <div class="smk-card">
            <h3>📋 Karakteristik Struktur Balok</h3>
            <ul>
                <li><b>Sisi:</b> Memiliki 3 pasang bidang berbentuk persegi panjang yang saling berhadapan dan kongruen.</li>
                <li><b>Dimensi Utama:</b> Ditentukan oleh variabel Panjang ($p$), Lebar ($l$), dan Tinggi ($t$).</li>
                <li><b>Sifat Tegak Lurus:</b> Setiap rusuk yang bertemu di satu titik sudut saling membentuk sudut $90^\circ$.</li>
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
        st.latex(r"Diag. \ Bidang \ Alas \ (D_{b1}) = \sqrt{p^2 + l^2}")
        st.latex(r"Diagonal \ Ruang \ (D_r) = \sqrt{p^2 + l^2 + t^2}")
        
        st.markdown("### 🧮 Lab Parameter Digital")
        p = st.number_input("Masukkan Panjang (p):", min_value=1.0, value=6.0, step=1.0)
        l = st.number_input("Masukkan Lebar (l):", min_value=1.0, value=4.0, step=1.0)
        t = st.number_input("Masukkan Tinggi (t):", min_value=1.0, value=3.0, step=1.0)
        
        # Perhitungan Metrik Balok
        v_balok = p * l * t
        lp_balok = 2 * ((p * l) + (p * t) + (l * t))
        db_alas = np.sqrt(p**2 + l**2)
        dr_balok = np.sqrt(p**2 + l**2 + t**2)
        
        st.success(f"📊 **Hasil Analisis Struktur Balok:**\n\n"
                   f"🔹 **Volume (V):** {v_balok:.2f} satuan kubik\n\n"
                   f"🔹 **Luas Permukaan (L):** {lp_balok:.2f} satuan persegi\n\n"
                   f"◼️ **Panjang Diagonal Alas:** {db_alas:.4f} satuan\n\n"
                   f"🚀 **Panjang Diagonal Ruang:** {dr_balok:.4f} satuan")

    with col2:
        st.markdown("### 🌐 Model Proyeksi 3D")
        st.caption("Gunakan kursor untuk memutar, menggeser, atau memperbesar proyeksi balok.")
        
        x = [0, p, p, 0, 0, p, p, 0]
        y = [0, 0, l, l, 0, 0, l, l]
        z = [0, 0, 0, 0, t, t, t, t]
        
        xl, yl, zl = get_wireframe_data(x, y, z)
        
        fig = go.Figure()
        
        # Plot Objek 3D (Solid transparan)
        fig.add_trace(go.Mesh3d(
            x=x, y=y, z=z,
            i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 2],
            opacity=0.3,
            color='#198754',
            flatshading=True,
            name="Volume"
        ))
        
        # Plot Kerangka (Wireframe)
        fig.add_trace(go.Scatter3d(
            x=xl, y=yl, zl=zl,
            mode='lines',
            line=dict(color='#198754', width=4),
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
                xaxis=dict(title='X (Panjang)', range=[-1, p+2], backgroundcolor="#f8f9fa"),
                yaxis=dict(title='Y (Lebar)', range=[-1, l+2], backgroundcolor="#f8f9fa"),
                zaxis=dict(title='Z (Tinggi)', range=[-1, t+2], backgroundcolor="#f8f9fa")
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
