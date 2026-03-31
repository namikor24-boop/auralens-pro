import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import base64
from fpdf import FPDF

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro", page_icon="🔮", layout="centered")

# Tema Gelap untuk Estetika Cozy
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    .stTextInput>div>div>input { background-color: #262730; color: #FFFFFF; }
    .stSelectbox>div>div>div { background-color: #262730; color: #FFFFFF; }
    div.stButton > button:first-child { background-color: #4B0082; color: #FFFFFF; border: none;}
    div.stAlert { background-color: #262730; color: #FFFFFF; border: none;}
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: AI Visualizer")
st.markdown("### Temukan Energi Karir & Penyeimbang Dirimu")

# --- DATABASE AURA (LOGIKA PRODUK & SARAN) ---
AURA_DATABASE = {
    "Merah": {
        "warna_hex": "#FF0000",
        "deskripsi": "Energi Berani & Semangat tinggi!",
        "analisis": "Kamu adalah eksekutor alami. Penuh gairah dan berani mengambil risiko.",
        "karir": "Eksekutor, Sales, Atlet, Pemimpin Proyek.",
        "hewan": "Kucing (Menenangkan)",
        "benda": "Kristal Amethyst"
    },
    "Emas": {
        "warna_hex": "#FFD700",
        "deskripsi": "Energi Kelimpahan & Hikmat!",
        "analisis": "Kamu memiliki aura kepemimpinan alami. Bijaksana, karismatik, dan menginspirasi.",
        "karir": "CEO, Mentor, Penulis, Pengambil Keputusan.",
        "hewan": "Kuda (Kekuatan & Kebebasan)",
        "benda": "Jam Tangan Logam"
    },
    "Cyan": {
        "warna_hex": "#00FFFF",
        "deskripsi": "Energi Damai & Komunikasi!",
        "analisis": "Kamu adalah penyembuh alami dan pembicara yang baik. Membawa kedamaian.",
        "karir": "HRD, Guru, Konselor, Jurnalis.",
        "hewan": "Burung (Kebebasan & Kreativitas)",
        "benda": "Mint Aromaterapi"
    },
    "Ungu": {
        "warna_hex": "#800080",
        "deskripsi": "Energi Kreativitas & Intuisi!",
        "analisis": "Kamu memiliki intuisi yang sangat kuat. Inovatif dan artistik.",
        "karir": "Desainer, Artis, Inovator, Peneliti.",
        "hewan": "Gajah (Kebijaksanaan & Kekuatan)",
        "benda": "Black Tourmaline"
    }
}

# --- SIDEBAR INPUT ---
with st.sidebar:
    st.header("Profil Pengguna")
    nama = st.text_input("Nama Lengkap", "")
    opsi_aura = st.selectbox("Pilih Warna Aura:", list(AURA_DATABASE.keys()))
    tombol_scan = st.button("Mulai Scan Aura Visual")

# --- LOGIKA UTAMA ---
if nama:
    st.write(f"### Halo, {nama}!")
    
    if tombol_scan:
        st.success(f"### Hasil Scan: Aura {opsi_aura}")
        
        # Fitur Ambil Foto (st.camera_input menampilkan foto kembali)
        foto = st.camera_input("Ambil foto untuk visualisasi auramu")
        
        if foto:
            # 1. MEMBUAT EFEK GLOW AURA VISUAL (Sihir Kita!)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img) # Memperbaiki orientasi (terutama HP)
            
            # Membuat pendaran warna (tint)
            color_hex = AURA_DATABASE[opsi_aura]["warna_hex"]
            # Konversi HEX ke RGB (misal #FF0000 -> (255, 0, 0))
            rgb_color = tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            
            aura_overlay = Image.new("RGB", img.size, rgb_color)
            combined = Image.blend(img, aura_overlay, alpha=0.3) # Efek transparan 30%
            
            # Meningkatkan kecerahan agar glowing
            enhancer = ImageEnhance.Brightness(combined)
            glowing_img = enhancer.enhance(1.2)
            
            # Menampilkan Foto dengan Efek Aura (WAJIB ADA!)
            st.image(glowing_img, caption=f"Visualisasi Aura {opsi_aura} - {nama}")
            
            # 2. MENAMPILKAN SARAN & ANALISIS (Yang Mbak Ayi Minta!)
            data = AURA_DATABASE[opsi_aura]
            st.divider()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"*Vibrasi Dominan:* {data['deskripsi']}")
                st.write(f"*Analisis:* {data['analisis']}")
                st.success(f"💼 *Karir Cocok:* {data['karir']}")

            with col2:
                st.warning(f"⚖️ *Penyeimbang Aura*")
                st.write(f"🐾 *Hewan:* {data['hewan']}")
                st.write(f"💎 *Benda:* {data['benda']}")
            
            st.balloons()
            
            # 3. FITUR PDF PREMIUM (UPSELL!)
            if st.button("Generate Premium Career Report (PDF)"):
                # Simpan foto glowing untuk dimasukkan ke PDF
                glowing_img.save("temp_aura_photo.jpg")
                
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 16)
                pdf.cell(200, 10, f"AuraLens Pro Report: {nama}", ln=True, align='C')
                
                pdf.set_font("Arial", size=12)
                pdf.ln(10)
                pdf.cell(200, 10, f"Warna Aura: {opsi_aura}", ln=True)
                pdf.cell(200, 10, f"Rekomendasi Karir: {data['karir']}", ln=True)
                pdf.cell(200, 10, f"Penyeimbang: {data['hewan']} & {data['benda']}", ln=True)
                
                # Tambahkan foto glowing ke PDF
                pdf.image("temp_aura_photo.jpg", x=50, y=70, w=100)
                
                pdf_output = pdf.output(dest='S').encode('latin-1')
                b64 = base64.b64encode(pdf_output).decode()
                href = f'<a href="data:application/pdf;base64,{b64}" download="Laporan_Aura_{nama}.pdf">Klik di sini untuk Download Laporanmu!</a>'
                st.markdown(href, unsafe_allow_html=True)
    else:
        st.info("Silakan klik tombol 'Mulai Scan Aura Visual' di menu samping.")
else:
    st.warning("Masukkan nama kamu di kolom sebelah kiri dulu ya!")
