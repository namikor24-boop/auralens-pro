import streamlit as st
from PIL import Image, ImageOps, ImageStat, ImageDraw, ImageFont
import time
import io

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

# CSS untuk tampilan gelap yang elegan
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700;
    }
    /* Style untuk kotak infografis di layar */
    .info-container {
        background-color: #1A1D24;
        border-radius: 20px;
        padding: 25px;
        border: 2px solid #30363D;
        margin-top: 20px;
        font-family: 'Courier New', Courier, monospace; /* Gaya tech/program */
    }
    .info-header {
        font-size: 28px;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .info-section {
        background-color: #21262D;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 5px solid;
    }
    .stat-label { color: #8B949E; font-size: 14px; }
    .stat-value { color: white; font-size: 20px; font-weight: bold; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #4B0082, #FFD700); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Analysis - Infographic Edition by Namikor")

# --- 2. DATABASE MASTER (INFOGRAFIS STYLE) ---
# Menyesuaikan data agar cocok dengan format infografis yang diminta
AURA_DB = {
    "Merah": {"hex": "#FF0000", "state": "Action / Intensity", "stres": 88, "vibrasi": "85 Hz", "deskripsi": "Kamu adalah pemrakarsa yang penuh energi fisik. Cenderung keras pada diri sendiri dan menyukai tantangan langsung.", "tips": "Upgrade skill sabar, latihan meditasi, dan hidup balance.", "partner": "Jingga, Kuning"},
    "Jingga": {"hex": "#FF7F00", "state": "Courage / Creativity", "stres": 75, "vibrasi": "72 Hz", "deskripsi": "Jiwa seni dan imajinasimu sangat kuat. Berani mengambil risiko, namun sering cemas penilaian orang.", "tips": "Upgrade skill komunikasi, portofolio kreatif, dan hidup balance.", "partner": "Merah, Kuning"},
    "Kuning": {"hex": "#FFFF00", "state": "Willingness / Logic", "stres": 86, "vibrasi": "82 Hz", "deskripsi": "Pemikir logis dan problem solver sejati. Kamu suka tantangan logika dari kode yang rumit.", "tips": "Upgrade skill upgrade, manajemen waktu, dan hidup balance.", "partner": "Biru, Hijau"},
    "Hijau": {"hex": "#00FF00", "state": "Reason / Harmony", "stres": 65, "vibrasi": "60 Hz", "deskripsi": "Penyembuh yang empati dan penyeimbang sekitar. Kehadiranmu menenangkan jiwa sekitar.", "tips": "Upgrade skill empati, time management, dan hidup balance.", "partner": "Kuning, Biru"},
    "Biru": {"hex": "#0000FF", "state": "Love / Clarity", "stres": 70, "vibrasi": "68 Hz", "deskripsi": "Penyampai pesan tulus dan damai. Menyatukan hati melalui kata-kata jujur.", "tips": "Upgrade skill public speaking, networking, dan hidup balance.", "partner": "Kuning, Hijau"},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy / Vision", "stres": 82, "vibrasi": "78 Hz", "deskripsi": "Visioner intuitif yang melihat masa depan. Merasa kesepian karena visimu yang berbeda.", "tips": "Upgrade skill inovasi, kolaborasi tim, dan hidup balance.", "partner": "Ungu, Putih"},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace / Wisdom", "stres": 60, "vibrasi": "55 Hz", "deskripsi": "Bijaksana, inovatif, dan spiritual. Menginspirasi transformasi global melalui cahaya.", "tips": "Upgrade skill leadership, mindfulness, dan hidup balance.", "partner": "Nila, Putih"}
}

# --- 3. INPUT DATA ---
nama = st.text_input("1. Nama Lengkap:", placeholder="Masukkan nama kamu...")
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

        st.success(f"Analisis Selesai! Aura Dominan: {warna_hasil}")
        
        # --- 4. TAMPILAN INFOGRAFIS DI LAYAR (HTML/CSS) ---
        # Ini dibuat agar mirip dengan gambar yang dikirim Mbak Ayi
        
        warna_hex = res["hex"]
        
        infografis_html = f"""
        <div class="info-container">
            <div class="info-header">NAMIKOR AURA BLUEPRINT</div>
            
            <div class="info-section" style="border-left-color: {warna_hex};">
                <div class="stat-label">Energi Kamu Match di Bidang</div>
                <div class="info-header" style="color: {warna_hex}; font-size: 32px; text-align: left; margin: 0;">{warna_hasil.upper()}</div>
                <p style="color: #A3B3C1; font-size: 14px; margin-top: 10px;">{res['deskripsi']}</p>
            </div>
            
            <div style="display: flex; gap: 15px; margin-bottom: 15px;">
                <div class="info-section" style="flex: 1; border-left-color: #FFD700; margin-bottom: 0;">
                    <div class="stat-label">Tingkat Stres</div>
                    <div class="stat-value" style="color: #FFD700; font-size: 36px;">{res['stres']}%</div>
                </div>
                <div class="info-section" style="flex: 1; border-left-color: #00FFFF; margin-bottom: 0;">
                    <div class="stat-label">Frekuensi Vibrasi</div>
                    <div class="stat-value" style="color: #00FFFF;">{res['vibrasi']}</div>
                </div>
            </div>
            
            <div class="info-section" style="border-left-color: #FFD700;">
                <div class="stat-label">Tips Sukses (Namikor)</div>
                <p style="color: white; font-size: 14px; font-weight: bold; margin: 5px 0;">{res['tips']}</p>
            </div>
            
            <div class="info-section" style="border-left-color: {warna_hex};">
                <div class="stat-label">Partner yang Cocok</div>
                <div class="stat-value">{res['partner']}</div>
            </div>

            <div style="text-align: center; color: #555; font-size: 10px; margin-top: 20px;">
                © 2026 Namikor. All Rights Reserved. ID: {nama[:3].upper()}-{umur}-{warna_hasil[:2].upper()}
            </div>
        </div>
        """
        st.markdown(infografis_html, unsafe_allow_html=True)
        
        st.info("💡 Tips: Screenshot tampilan di atas untuk menyimpan infografis Aura Namikor kamu!")

    st.caption("© 2026 Namikor. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama untuk memulai.")
