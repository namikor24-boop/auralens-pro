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
    .hawkins-box {
        font-size: 24px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; margin: 15px 0px;
    }
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border-left: 6px solid #FFD700; margin-top: 20px; }
    .warning-card { background-color: #2D1B1B; padding: 15px; border-radius: 10px; border-left: 6px solid #FF4B4B; margin-top: 10px; color: #FFCDCD; }
    .motivation-card { background-color: #1B2D1B; padding: 15px; border-radius: 10px; border-left: 6px solid #4BFF4B; margin-top: 10px; color: #CDFFCD; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #4B0082, #FFD700); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Life Blueprint Analysis - Version 3.0")

# --- DATABASE MASTER ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "tantangan": "Cenderung impulsif dan mudah marah jika keinginan tidak terpenuhi.", "solusi": "Salurkan energimu ke olahraga atau karya kreatif. Ingat, kesabaran adalah kekuatan yang tenang."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "tantangan": "Sering merasa cemas berlebihan tentang penilaian orang lain.", "solusi": "Fokuslah pada proses berkarya, bukan hasil akhir. Duniamu tetap indah meski tidak semua orang melihatnya."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "tantangan": "Terlalu banyak berpikir (overthinking) hingga lupa beraksi.", "solusi": "Ilmu tanpa amal itu hampa. Mulailah satu langkah kecil hari ini, jangan tunggu sempurna."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "tantangan": "Sering mendahulukan orang lain hingga mengabaikan diri sendiri.", "solusi": "Kamu tidak bisa menuang air dari gelas yang kosong. Cintai dirimu sendiri sebelum menyembuhkan dunia."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "tantangan": "Kadang sulit mengungkapkan perasaan jujur karena takut konflik.", "solusi": "Suaramu berharga. Berbicara jujur dengan kasih sayang akan membuka pintu yang selama ini tertutup."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "tantangan": "Merasa kesepian karena merasa tidak ada yang memahami visi besarmu.", "solusi": "Temukan komunitas yang sefrekuensi. Kamu tidak perlu berjalan sendirian untuk mencapai bintang."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "tantangan": "Bisa menjadi terlalu idealis dan jauh dari realita praktis.", "solusi": "Tetaplah membumi. Gunakan kebijaksanaanmu untuk membantu hal-hal nyata di sekitarmu."},
    "Abu-Abu": {"hex": "#808080", "hawkins": 250, "state": "Neutrality", "tantangan": "Kurang semangat dan merasa hidup terasa datar atau membosankan.", "solusi": "Cobalah hal baru di luar zona nyamanmu. Sedikit percikan keberanian akan mewarnai harimu."},
    "Marun": {"hex": "#800000", "hawkins": 175, "state": "Intensity", "tantangan": "Menyimpan tekanan batin yang kuat dan keras pada diri sendiri.", "solusi": "Maafkan kesalahan masa lalu. Kamu sedang berproses, dan itu sudah lebih dari cukup."},
    "Hitam": {"hex": "#1A1A1A", "hawkins": 100, "state": "Protection", "tantangan": "Menutup diri terlalu rapat karena takut disakiti kembali.", "solusi": "Perisai melindungimu, tapi juga menghalangimu melihat cahaya. Beranilah terbuka pada orang yang tepat."}
}

# --- 1. INPUT DATA ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Masukkan nama kamu...")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Pindai Prana & Energi Bio-Foton")

    if foto:
        # ANIMASI SCANNING
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            if i < 30: status_text.text("🧬 Mengumpulkan data biometric...")
            elif i < 60: status_text.text("⚡ Menganalisis frekuensi Hawkins...")
            else: status_text.text("🔮 Membuka Blueprint Aura...")
        
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        stat = ImageStat.Stat(img)
        brightness = sum(stat.mean) / 3 
        
        warna_keys = list(AURA_DB.keys())
        warna_hasil = warna_keys[int(brightness % len(warna_keys))]
        res = AURA_DB[warna_hasil]

        # VISUALISASI HASIL
        st.success(f"Analisis Selesai! Aura Dominan: {warna_hasil}")
        
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        st.image(visual, use_container_width=True)

        # HAWKINS & CHAKRA BARS
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | Status: {res["state"]}</div>', unsafe_allow_html=True)
        
        st.subheader("📊 Chakra Energy Balance")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("Energi Kreatif")
            st.progress(int((brightness % 40) + 60))
        with col_b:
            st.write("Ketenangan Batin")
            st.progress(int((res['hawkins'] / 700) * 100))

        # DUALITY DESCRIPTION
        st.markdown(f'<div class="warning-card">⚠️ <b>TANTANGAN:</b> {res["tantangan"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="motivation-card">✨ <b>REKOMENDASI:</b> {res["solusi"]}</div>', unsafe_allow_html=True)

        # DOWNLOAD PDF
        st.divider()
        if st.button("📥 Download Laporan Lengkap (PDF)"):
            # (Kode PDF tetap sama seperti sebelumnya)
            st.info("Fitur PDF sedang menyiapkan file...")
            # ... tambahkan logika PDF Mbak Ayi di sini ...
            
    st.caption("© 2026 Namikor. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama untuk memulai.")
