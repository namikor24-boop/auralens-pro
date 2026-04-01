import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
from fpdf import FPDF

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700;
    }
    .hawkins-box {
        font-size: 24px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; margin: 15px 0px;
    }
    .warning-card { background-color: #2D1B1B; padding: 15px; border-radius: 10px; border-left: 6px solid #FF4B4B; margin-top: 10px; color: #FFCDCD; }
    .motivation-card { background-color: #1B2D1B; padding: 15px; border-radius: 10px; border-left: 6px solid #4BFF4B; margin-top: 10px; color: #CDFFCD; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Life Blueprint Analysis - By Namikor")

# --- 2. DATABASE MASTER ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "tantangan": "Mudah marah & impulsif.", "solusi": "Salurkan energi ke olahraga. Kesabaran adalah kekuatan yang tenang."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "tantangan": "Sering cemas penilaian orang.", "solusi": "Fokus pada proses, duniamu indah apa adanya."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "tantangan": "Terlalu banyak berpikir.", "solusi": "Mulailah langkah kecil sekarang juga."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "tantangan": "Sering lupa mencintai diri sendiri.", "solusi": "Istirahat sejenak, kamu berhak bahagia."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "tantangan": "Takut jujur karena konflik.", "solusi": "Bicaralah dari hati, suaramu sangat berharga."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "tantangan": "Merasa kesepian dengan visimu.", "solusi": "Cari teman sefrekuensi untuk berbagi ide."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "tantangan": "Terlalu idealis.", "solusi": "Bantu hal nyata yang ada di depan mata."},
    "Abu-Abu": {"hex": "#808080", "hawkins": 250, "state": "Neutrality", "tantangan": "Hidup terasa datar.", "solusi": "Coba satu hal baru yang menantang."},
    "Marun": {"hex": "#800000", "hawkins": 175, "state": "Intensity", "tantangan": "Sangat keras pada diri sendiri.", "solusi": "Maafkan masa lalu, kamu sedang berproses."},
    "Hitam": {"hex": "#1A1A1A", "hawkins": 100, "state": "Protection", "tantangan": "Takut disakiti kembali.", "solusi": "Beranilah terbuka pada hal baik di sekitarmu."}
}

# --- 3. INPUT DATA ---
nama = st.text_input("1. Nama Lengkap:", placeholder="Masukkan nama...")
umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Ambil Foto Aura")

    if foto:
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        stat = ImageStat.Stat(img)
        brightness = sum(stat.mean) / 3 
        
        warna_keys = list(AURA_DB.keys())
        warna_hasil = warna_keys[int(brightness % len(warna_keys))]
        res = AURA_DB[warna_hasil]

        st.success(f"Analisis Selesai! Aura: {warna_hasil}")
        
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        st.image(visual, use_container_width=True)

        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | Status: {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="warning-card">⚠️ <b>TANTANGAN:</b> {res["tantangan"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="motivation-card">✨ <b>REKOMENDASI:</b> {res["solusi"]}</div>', unsafe_allow_html=True)

        # --- PROSES PDF ---
        visual.save("temp_aura.jpg")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_fill_color(14, 17, 23)
        pdf.rect(0, 0, 210, 297, 'F')
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 20, "NAMIKOR AURA LENS REPORT", ln=True, align='C')
        pdf.image("temp_aura.jpg", x=55, y=40, w=100)
        pdf.ln(100)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Nama: {nama}", ln=True)
        pdf.cell(0, 10, f"Warna Aura: {warna_hasil}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 8, f"Saran Namikor: {res['solusi']}")
        pdf.ln(10)
        pdf.cell(0, 10, "© 2026 Namikor. All Rights Reserved.", ln=True, align='C')
        
        pdf_out = pdf.output(dest='S').encode('latin-1')

        st.download_button(
            label="📥 DOWNLOAD LAPORAN PDF (NAMIKOR)",
            data=pdf_out,
            file_name=f"Aura_Namikor_{nama}.pdf",
            mime="application/pdf"
        )

    st.caption("© 2026 Namikor. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama.")
