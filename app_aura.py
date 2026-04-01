import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import base64
from fpdf import FPDF

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

# CSS untuk tampilan keren
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
st.caption("Advanced Biometric Life Blueprint Analysis - Version 3.0")

# --- 2. DATABASE MASTER ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "tantangan": "Cenderung impulsif dan mudah marah.", "solusi": "Salurkan energimu ke olahraga. Kesabaran adalah kekuatan yang tenang."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "tantangan": "Sering merasa cemas berlebihan.", "solusi": "Fokuslah pada proses berkarya. Duniamu indah apa adanya."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "tantangan": "Terlalu banyak berpikir (overthinking).", "solusi": "Mulailah satu langkah kecil hari ini. Jangan tunggu sempurna."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "tantangan": "Sering mengabaikan diri sendiri demi orang lain.", "solusi": "Cintai dirimu sendiri. Kamu berhak untuk bahagia."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "tantangan": "Sulit jujur karena takut konflik.", "solusi": "Suaramu berharga. Berbicara jujur akan membuka pintu kesuksesan."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "tantangan": "Merasa kesepian karena visi besarmu.", "solusi": "Cari teman sefrekuensi. Kamu tidak perlu berjalan sendirian."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "tantangan": "Terlalu idealis dan jauh dari realita.", "solusi": "Tetaplah membumi. Bantu hal-hal nyata di sekitarmu."},
    "Abu-Abu": {"hex": "#808080", "hawkins": 250, "state": "Neutrality", "tantangan": "Merasa hidup terasa datar atau membosankan.", "solusi": "Coba hal baru. Sedikit keberanian akan mewarnai harimu."},
    "Marun": {"hex": "#800000", "hawkins": 175, "state": "Intensity", "tantangan": "Keras pada diri sendiri.", "solusi": "Maafkan masa lalu. Kamu sedang berproses, itu sudah cukup."},
    "Hitam": {"hex": "#1A1A1A", "hawkins": 100, "state": "Protection", "tantangan": "Menutup diri karena takut disakiti.", "solusi": "Beranilah terbuka pada hal-hal baik di sekitarmu."}
}

# --- 3. INPUT DATA ---
nama = st.text_input("1. Nama Lengkap:", placeholder="Masukkan nama...")
umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Pindai Prana & Energi Bio-Foton")

    if foto:
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        stat = ImageStat.Stat(img)
        brightness = sum(stat.mean) / 3 
        
        warna_keys = list(AURA_DB.keys())
        warna_hasil = warna_keys[int(brightness % len(warna_keys))]
        res = AURA_DB[warna_hasil]

        st.success(f"Analisis Selesai! Aura Dominan: {warna_hasil}")
        
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        st.image(visual, use_container_width=True)

        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | Status: {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="warning-card">⚠️ <b>TANTANGAN:</b> {res["tantangan"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="motivation-card">✨ <b>REKOMENDASI:</b> {res["solusi"]}</div>', unsafe_allow_html=True)

    st.caption("© 2026 Hikari Salsabila Syauqi. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama untuk memulai.")
