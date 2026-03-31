import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import base64
from fpdf import FPDF

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro - Digital Product", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700; 
    }
    .hawkins-box {
        font-size: 28px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 15px; border: 2px solid #FFD700; margin: 10px 0px;
    }
    .spectrum-bar { height: 15px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin: 15px 0px; }
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border: 1px solid #4B0082; margin-top: 20px; }
    .copyright-text { text-align: center; font-size: 12px; color: #666; margin-top: 50px; border-top: 1px solid #333; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Life Blueprint")
st.caption("“Official Digital Product by Hikari Salsabila Syauqi”")

# Database Aura
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "vibrasi": "Api", "blueprint": "Pemberani & Pelopor.", "hobi": "Bela Diri.", "hewan": "Anjing.", "karir": "Atlet/CEO."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "vibrasi": "Kreatif", "blueprint": "Pencipta Ekspresif.", "hobi": "Seni Digital.", "hewan": "Kucing.", "karir": "Artis/Creator."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "vibrasi": "Logika", "blueprint": "Pemikir Analitis.", "hobi": "Catur/Coding.", "hewan": "Burung.", "karir": "Programmer/Ilmuwan."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "vibrasi": "Harmoni", "blueprint": "Penyembuh Penyeimbang.", "hobi": "Berkebun.", "hewan": "Ikan.", "karir": "Dokter/Arsitek."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "vibrasi": "Air", "blueprint": "Komunikator Damai.", "hobi": "Bernyanyi.", "hewan": "Golden Retriever.", "karir": "Diplomat/Guru."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "vibrasi": "Intuisi", "blueprint": "Visioner Intuitif.", "hobi": "Astronomi.", "hewan": "Kucing Siam.", "karir": "Inovator."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "vibrasi": "Eterik", "blueprint": "Bijaksana Inovatif.", "hobi": "Yoga/Filsafat.", "hewan": "Kuda.", "karir": "Visioner Tech."}
}

# --- 1. INPUT ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Scan Bio-Energy")

    if foto:
        with st.status("🧬 Generating Life Blueprint...", expanded=False):
            time.sleep(1)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            warna_hasil = list(AURA_DB.keys())[int(brightness % 7)]
            res = AURA_DB[warna_hasil]

        # Efek Aura
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        
        st.subheader(f"Hasil Analisis: Aura {warna_hasil}")
        st.image(visual)
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # FITUR PRINT PDF
        if st.button("📥 Download Official Digital Report (PDF)"):
            visual.save("temp_aura.jpg")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_fill_color(14, 17, 23)
            pdf.rect(0, 0, 210, 297, 'F')
            pdf.set_text_color(255, 255, 255)
            
            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 20, "AURA LENS PRO: OFFICIAL REPORT", ln=True, align='C')
            pdf.set_font("Arial", '', 12)
            pdf.cell(0, 10, f"Name: {nama} | Age: {umur}", ln=True, align='C')
            pdf.ln(10)
            
            pdf.image("temp_aura.jpg", x=55, y=50, w=100)
            pdf.ln(110)
            
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, f"Energy Result: {warna_hasil} ({res['hawkins']} Log)", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 10, f"Blueprint: {res['blueprint']}")
            pdf.multi_cell(0, 10, f"Hobby: {res['hobi']} | Pet: {res['hewan']}")
            pdf.multi_cell(0, 10, f"Career Path: {res['karir']}")
            
            pdf.ln(20)
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 10, "Copyright 2026 Namikor. All Rights Reserved.", ln=True, align='C')
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="Report_{nama}.pdf" style="color:white; text-decoration:none; background:#4B0082; padding:10px; border-radius:5px;">Klik di sini untuk mengunduh PDF Anda</a>'
            st.markdown(href, unsafe_allow_html=True)

    st.markdown(f'<div class="copyright-text">© 2026 <b>Hikari Salsabila Syauqi</b>. All Rights Reserved.</div>', unsafe_allow_html=True)
else:
    st.info("Sistem Standby. Masukkan nama.")
