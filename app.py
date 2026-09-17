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
