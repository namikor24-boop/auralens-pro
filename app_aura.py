# --- FITUR DOWNLOAD PDF PREMIUM ---
        if st.button("📥 Download Official Digital Report (PDF)"):
            visual.save("temp_aura.jpg")
            pdf = FPDF()
            pdf.add_page()
            
            # 1. Background Gelap (Futuristik)
            pdf.set_fill_color(14, 17, 23)
            pdf.rect(0, 0, 210, 297, 'F')
            
            # 2. Header: Judul Laporan
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Arial", 'B', 22)
            pdf.cell(0, 20, "AURA LENS PRO: OFFICIAL REPORT", ln=True, align='C')
            
            # 3. Sub-Header: Identitas Pengguna
            pdf.set_font("Arial", '', 12)
            pdf.set_text_color(200, 200, 200)
            pdf.cell(0, 10, f"Subject: {nama} | Age: {umur} Years", ln=True, align='C')
            pdf.ln(10)
            
            # 4. Foto Hasil Scan (Berbingkai)
            # Menghitung posisi tengah
            pdf.image("temp_aura.jpg", x=55, y=55, w=100)
            pdf.ln(110)
            
            # 5. Blok Data Hasil Scan (Seperti di Gambar)
            pdf.set_fill_color(30, 30, 40)
            pdf.rect(20, 165, 170, 75, 'F') # Kotak Info
            
            pdf.set_xy(25, 175)
            pdf.set_font("Arial", 'B', 14)
            pdf.set_text_color(0, 255, 255) # Warna Cyan (Futuristik)
            pdf.cell(0, 10, f"HASIL SCAN AURA LENS PRO", ln=True)
            
            pdf.set_font("Arial", '', 12)
            pdf.set_text_color(255, 255, 255)
            pdf.set_xy(25, 185)
            pdf.cell(0, 10, f"Warna Dominan: {warna_hasil} (Inti Hawkins {res['hawkins']} Log)", ln=True)
            
            pdf.set_xy(25, 195)
            # Simulasi Bio-vibrasi berdasarkan kecerahan foto
            bio_hz = int(brightness * 2.5) 
            pdf.cell(0, 10, f"Bio-Vibrasi: {bio_hz} Hz", ln=True)
            
            pdf.set_xy(25, 205)
            pdf.multi_cell(160, 8, f"Analisis: {res['blueprint']}")
            
            # 6. Informasi Karir/Belajar (Life Path)
            pdf.ln(15)
            pdf.set_xy(25, 225)
            pdf.set_text_color(255, 215, 0) # Warna Emas
            path_text = res['belajar'] if umur <= 18 else res['karir']
            pdf.cell(0, 10, f"Life Path Recommendation: {path_text}", ln=True)
            
            # 7. Copyright Footer (Hak Cipta Namikor)
            pdf.set_y(270)
            pdf.set_font("Arial", 'I', 10)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(0, 10, "Copyright 2026 Hikari Salsabila Syauqi. All Rights Reserved.", ln=True, align='C')
            
            # 8. Proses Output
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            
            # Tombol Link Download
            download_html = f'''
                <div style="text-align:center; margin-top:20px;">
                    <a href="data:application/pdf;base64,{b64}" download="AuraReport_{nama}.pdf" 
                       style="background-color: #4B0082; color: white; padding: 15px 25px; 
                       text-decoration: none; border-radius: 10px; font-weight: bold; border: 2px solid #FFD700;">
                       📥 KLIK DISINI UNTUK UNDUH PDF LAPORAN
                    </a>
                </div>
            '''
            st.markdown(download_html, unsafe_allow_html=True)
