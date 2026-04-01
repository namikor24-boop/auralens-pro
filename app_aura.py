import streamlit as st
from PIL import Image, ImageOps, ImageStat
from fpdf import FPDF
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700;
    }
    .info-box {
        background: linear-gradient(45deg, #1A1D24, #0E1117);
        border-radius: 15px; padding: 20px; border: 2px solid #30363D; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Infographic Blueprint Edition - By Namikor")

# --- 2. DATABASE MASTER (INFOGRAFIS DATA) ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "stres": "86%", "vibe": "85Hz", "bidang": "PHYSICAL ACTION", "tips": "Upgrade skill sabar & portofolio fisik.", "partner": "Jingga, Kuning"},
    "Jingga": {"hex": "#FF7F00", "stres": "75%", "vibe": "72Hz", "bidang": "CREATIVE ARTS", "tips": "Fokus pada imajinasi & komunikasi oke.", "partner": "Merah, Kuning"},
    "Kuning": {"hex": "#FFFF00", "stres": "86%", "vibe": "82Hz", "bidang": "PROGRAMMING", "tips": "Upgrade skill logic & upgrade portofolio.", "partner": "Biru, Hijau"},
    "Hijau": {"hex": "#00FF00", "stres": "60%", "vibe": "65Hz", "bidang": "HEALTH & CARE", "tips": "Upgrade empati & hidup balance.", "partner": "Kuning, Biru"},
    "Biru": {"hex": "#0000FF", "stres": "65%", "vibe": "68Hz", "bidang": "COMMUNICATION", "tips": "Upgrade public speaking & kejujuran.", "partner": "Kuning, Hijau"},
    "Nila": {"hex": "#4B0082", "stres": "82%", "vibe": "78Hz", "bidang": "INNOVATION", "tips": "Fokus pada visi & kolaborasi tech.", "partner": "Ungu, Putih"},
    "Ungu": {"hex": "#800080", "stres": "55%", "vibe": "60Hz", "bidang": "SPIRITUAL TECH", "tips": "Upgrade leadership & mindfulness.", "partner": "Nila, Putih"}
}

# --- 3. INPUT DATA ---
nama = st.text_input("Nama Lengkap:", placeholder="Contoh: Mbak Ayi")
umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    foto = st.camera_input("Scan Energi Kamu")

    if foto:
        with st.status("🧬 Generating Infographic...", expanded=True) as status:
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            warna_keys = list(AURA_DB.keys())
            warna_hasil = warna_keys[int(brightness % len(warna_keys))]
            res = AURA_DB[warna_hasil]
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete")

        st.subheader(f"Energi Kamu Match di Bidang: {res['bidang']}")
        
        # --- PDF GENERATOR (GAYA INFOGRAFIS) ---
        pdf = FPDF()
        pdf.add_page()
        
        # Background Gelap
        pdf.set_fill_color(14, 17, 23)
        pdf.rect(0, 0, 210, 297, 'F')
        
        # Header Box
        pdf.set_fill_color(30, 35, 45)
        pdf.rect(10, 10, 190, 40, 'F')
        pdf.set_draw_color(255, 215, 0) # Gold
        pdf.rect(10, 10, 190, 40)
        
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Arial", 'B', 10)
        pdf.set_xy(15, 15)
        pdf.cell(0, 5, "NAMIKOR AURA BLUEPRINT v3.0", ln=True)
        pdf.set_font("Arial", 'B', 24)
        pdf.set_xy(15, 22)
        pdf.cell(0, 15, res['bidang'], ln=True)
        
        # Foto Aura (Diatur agar estetik)
        visual = Image.blend(img, Image.new("RGB", img.size, tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))), alpha=0.3)
        visual.save("aura_pdf.jpg")
        pdf.image("aura_pdf.jpg", x=130, y=15, w=60)

        # Bar Tingkat Stres (Visual Grafis)
        pdf.set_xy(10, 60)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Tingkat Stres: {res['stres']}", ln=True)
        
        # Bar Background
        pdf.set_fill_color(50, 50, 50)
        pdf.rect(10, 70, 100, 5, 'F')
        # Bar Value (Warna sesuai Aura)
        r, g, b = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        pdf.set_fill_color(r, g, b)
        pdf.rect(10, 70, int(res['stres'].replace('%','')), 5, 'F')

        # Tips Sukses Box
        pdf.set_fill_color(25, 30, 40)
        pdf.rect(10, 85, 190, 30, 'F')
        pdf.set_xy(15, 90)
        pdf.set_text_color(0, 255, 255) # Cyan
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(0, 5, "TIPS SUKSES:", ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", '', 10)
        pdf.set_xy(15, 96)
        pdf.multi_cell(180, 6, res['tips'])

        # Bonus Partner Section
        pdf.set_xy(10, 125)
        pdf.set_font("Arial", 'B', 12)
        pdf.set_text_color(255, 215, 0)
        pdf.cell(0, 10, "BONUS! Partner In Crime:", ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", '', 11)
        pdf.cell(0, 8, res['partner'], ln=True)

        # Footer
        pdf.set_xy(10, 270)
        pdf.set_draw_color(100, 100, 100)
        pdf.line(10, 275, 200, 275)
        pdf.set_font("Arial", 'I', 8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 10, "OFFICIAL NAMIKOR REPORT - © 2026 Namikor All Rights Reserved", align='C')

        # Export PDF
        pdf_data = pdf.output(dest='S')
        if isinstance(pdf_data, str):
            pdf_data = pdf_data.encode('latin-1')

        st.download_button(
            label="📥 DOWNLOAD INFOGRAPHIC PDF (NAMIKOR)",
            data=pdf_data,
            file_name=f"Namikor_Blueprint_{nama}.pdf",
            mime="application/pdf"
        )
        
        st.info("💡 PDF ini didesain otomatis menyerupai kartu portofolio Namikor!")

    st.caption("© 2026 Namikor. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama.")
