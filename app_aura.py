import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import base64
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
    
    /* RUMAH KAMERA & OVAL */
    .camera-wrapper {
        position: relative;
        width: 100%;
        margin-top: 20px;
    }

    /* OVAL PANDUAN - Sekarang posisinya relatif terhadap kotak kamera */
    .face-guide {
        position: absolute;
        top: 40%;  /* Geser sedikit ke atas dari tengah */
        left: 50%;
        transform: translate(-50%, -50%);
        width: 180px;
        height: 240px;
        border: 3px dashed #FFD700;
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        z-index: 99;
        pointer-events: none; /* Supaya tombol 'Take Photo' tetap bisa diklik */
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
    }

    .guide-label {
        position: absolute;
        bottom: 25%;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(75, 0, 130, 0.8);
        color: #FFD700;
        padding: 4px 12px;
        border-radius: 10px;
        font-size: 11px;
        z-index: 100;
        white-space: nowrap;
        pointer-events: none;
    }

    .hawkins-box {
        font-size: 24px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; margin: 15px 0px;
    }
    .spectrum-bar { height: 12px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin: 15px 0px; }
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border-left: 6px solid #FFD700; margin-top: 20px; }
    .copyright { text-align: center; font-size: 12px; color: #888; margin-top: 50px; border-top: 1px solid #333; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Life Blueprint Analysis - By Namikor")

# Database Master
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "blueprint": "Pelopor Berani & Tak Kenal Takut."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "blueprint": "Pencipta Ekspresif & Bersemangat."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "blueprint": "Pemikir Logis & Cerdas."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "blueprint": "Penyembuh Penyeimbang & Empati."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "blueprint": "Penyampai Pesan Tulus & Damai."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "blueprint": "Visioner Intuitif."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "blueprint": "Bijaksana Inovatif & Spiritual."}
}

# --- 1. INPUT DATA ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    
    # --- BAGIAN KAMERA DENGAN OVAL YANG SUDAH DIPERBAIKI ---
    st.markdown('<div class="camera-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="face-guide"></div><div class="guide-label">POSISIKAN WAJAH DI SINI</div>', unsafe_allow_html=True)
    
    foto = st.camera_input("2. Pindai Prana & Energi Bio-Foton")
    
    st.markdown('</div>', unsafe_allow_html=True)
    # -------------------------------------------------------

    if foto:
        with st.status("🧬 Memproses Energi...", expanded=False) as status:
            time.sleep(1.5)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            warna_keys = list(AURA_DB.keys())
            warna_hasil = warna_keys[int(brightness % 7)]
            res = AURA_DB[warna_hasil]
            status.update(label=f"Aura {warna_hasil} Teridentifikasi!", state="complete")

        # Visualisasi Aura
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        
        st.subheader(f"Hasil Analisis: Aura {warna_hasil}")
        st.image(visual, use_container_width=True)
        
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | Status: {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # 5. BLUEPRINT
        st.markdown(f"""
        <div class="blueprint-card">
        <h3 style='color:#FFD700; margin-top:0;'>🧬 My Life Blueprint</h3>
        <p><b>Jati Diri:</b> {res['blueprint']}</p>
        </div>
        """, unsafe_allow_html=True)

        # 6. DOWNLOAD PDF
        st.divider()
        if st.button("📥 Download Laporan PDF"):
            visual.save("temp_aura.jpg")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_fill_color(14, 17, 23)
            pdf.rect(0, 0, 210, 297, 'F')
            pdf.set_text_color(255, 215, 0)
            pdf.set_font("Arial", 'B', 18)
            pdf.cell(0, 20, "NAMIKOR AURA REPORT", ln=True, align='C')
            
            pdf_out = pdf.output(dest='S')
            if isinstance(pdf_out, str): pdf_out = pdf_out.encode('latin-1')
            
            st.download_button(
                label="KLIK UNTUK SIMPAN PDF",
                data=pdf_out,
                file_name=f"Aura_Namikor_{nama}.pdf",
                mime="application/pdf"
            )

    st.markdown(f'<div class="copyright">© 2026 <b>Namikor</b>. All Rights Reserved.</div>', unsafe_allow_html=True)
else:
    st.info("Sistem Standby. Silahkan masukkan nama untuk memulai.")
