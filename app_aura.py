import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import io

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

# CSS UPGRADE: RADIANCE EDITION (Mengejar Vibe AURA Scope)
st.markdown("""
    <style>
    /* Gradient Background yang Misterius */
    .stApp {
        background: linear-gradient(180deg, #0A0F1E 0%, #17203A 100%);
        color: white;
        font-family: 'Inter', sans-serif; /* Font modern */
    }
    
    /* Judul Utama */
    h1 {
        text-align: center;
        color: #FFD700;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
    }
    
    /* Tombol Utama yang 'Glow' */
    div.stButton > button:first-child { 
        width: 100%; 
        background: linear-gradient(90deg, #6200EA, #AA00FF);
        color: white; 
        border-radius: 30px; /* Lebih bulat */
        font-weight: bold; 
        border: none;
        font-size: 16px;
        padding: 12px 0;
        box-shadow: 0 4px 15px rgba(170, 0, 255, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 6px 20px rgba(170, 0, 255, 0.6);
        transform: translateY(-2px);
    }

    /* KOTAK INFOGRAFIS DI LAYAR */
    .info-container {
        background-color: rgba(26, 29, 36, 0.8); /* Transparan dikit */
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 25px;
        backdrop-filter: blur(10px); /* Efek kaca buram */
    }
    .info-header {
        font-size: 26px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    .info-section {
        background-color: rgba(33, 38, 45, 0.6);
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 15px;
        border-left: 6px solid;
    }
    .stat-label { color: #8B949E; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;}
    .stat-value { color: white; font-size: 22px; font-weight: bold; }
    
    /* Progress Bar Kustom */
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #AA00FF, #FFD700); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Analysis - By Namikor")

# --- 2. DATABASE MASTER (INFOGRAFIS STYLE) ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "vibrasi": "85 Hz", "deskripsi": "Pemrakarsa energi fisik penuh aksi.", "tips": "Latihan meditasi & sabar.", "partner": "Jingga, Kuning", "vibe": "Pure Action"},
    "Jingga": {"hex": "#FF7F00", "vibrasi": "72 Hz", "deskripsi": "Jiwa seni kreatif & berani.", "tips": "Portofolio kreatif & hidup balance.", "partner": "Merah, Kuning", "vibe": "Vibrant Soul"},
    "Kuning": {"hex": "#FFFF00", "vibrasi": "82 Hz", "deskripsi": "Pemikir logis & problem solver.", "tips": "Manajemen waktu & coding.", "partner": "Biru, Hijau", "vibe": "Logic Willingness"},
    "Hijau": {"hex": "#00FF00", "vibrasi": "60 Hz", "deskripsi": "Penyembuh empati & harmoni.", "tips": "Time management & empati.", "partner": "Kuning, Biru", "vibe": "Soft Healing"},
    "Biru": {"hex": "#0000FF", "vibrasi": "68 Hz", "deskripsi": "Penyampai pesan tulus & damai.", "tips": "Public speaking & kejujuran.", "partner": "Kuning, Hijau", "vibe": "Clear Communication"},
    "Nila": {"hex": "#4B0082", "vibrasi": "78 Hz", "deskripsi": "Visioner intuitif masa depan.", "tips": "Inovasi & kolaborasi tim.", "partner": "Ungu, Putih", "vibe": "Mystic Joy"},
    "Ungu": {"hex": "#800080", "vibrasi": "55 Hz", "deskripsi": "Bijaksana, inovatif, & spiritual.", "tips": "Leadership & mindfulness.", "partner": "Nila, Putih", "vibe": "Peaceful Wisdom"}
}

# --- 3. INPUT DATA ---
nama = st.text_input("1. Nama Lengkap:", placeholder="Masukkan nama kamu...")
umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Ambil Foto Aura ✨")

    if foto:
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        stat = ImageStat.Stat(img)
        brightness = sum(stat.mean) / 3 
        
        warna_keys = list(AURA_DB.keys())
        warna_hasil = warna_keys[int(brightness % len(warna_keys))]
        res = AURA_DB[warna_hasil]

        st.success(f"Analisis Selesai! Aura Dominan: {warna_hasil} ✨")
        
        # --- 4. TAMPILAN INFOGRAFIS DI LAYAR (HTML/CSS Upgrade) ---
        warna_hex = res["hex"]
        
        infografis_html = f"""
        <div class="info-container">
            <div class="info-header">✨ NAMIKOR AURA BLUEPRINT</div>
            
            <div class="info-section" style="border-left-color: {warna_hex}; background-color: rgba(33, 38, 45, 0.4);">
                <div class="stat-label">Aura Dominan</div>
                <div class="info-header" style="color: {warna_hex}; font-size: 36px; text-align: left; margin: 0; text-transform: none;">{warna_hasil}</div>
                <div class="stat-value" style="font-size: 14px; color: #FFD700; margin-top: 5px;">Status: {res['vibe']}</div>
                <p style="color: #A3B3C1; font-size: 14px; margin-top: 15px;">{res['deskripsi']}</p>
            </div>
            
            <div class="info-section" style="border-left-color: #00FFFF;">
                <div class="stat-label">Frekuensi Vibrasi</div>
                <div class="stat-value" style="color: #00FFFF; font-size: 28px;">{res['vibrasi']}</div>
            </div>
            
            <div class="info-section" style="border-left-color: #FFD700;">
                <div class="stat-label">Rekomendasi Sukses (Namikor) ✨</div>
                <p style="color: white; font-size: 15px; font-weight: bold; margin: 8px 0;">{res['tips']}</p>
            </div>
            
            <div class="info-section" style="border-left-color: {warna_hex}; margin-bottom: 0;">
                <div class="stat-label">Partner yang Cocok</div>
                <div class="stat-value" style="font-size: 16px;">{res['partner']}</div>
            </div>

            <div style="text-align: center; color: #555; font-size: 10px; margin-top: 25px; letter-spacing: 1px;">
                ID: {nama[:3].upper()}-{umur}-{warna_hasil[:2].upper()} | OFFICIAL REPORT BY NAMIKOR
            </div>
        </div>
        """
        st.markdown(infografis_html, unsafe_allow_html=True)
        
        st.info("💡 Tips: Screenshot tampilan di atas untuk menyimpan infografis Aura Namikor kamu yang keren ini!")

    st.caption("© 2026 Namikor. All Rights Reserved.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama untuk memulai.")
