import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro - Official Copyright", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; 
        background-color: #4B0082; 
        color: white; 
        border-radius: 12px; 
        font-weight: bold; 
        border: 2px solid #FFD700; 
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
st.caption("“Membaca frekuensi energi biometrik dan cetak biru jiwa Anda.”")

# Database Aura & Blueprint
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Action", "vibrasi": "Energi Api",
        "blueprint": "Pemberani & Pelopor. Anda lahir untuk membuka jalan bagi orang lain.",
        "hobi": "Olahraga berat.", "hewan": "Anjing Penjaga.", "karir": "Atlet/CEO."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "state": "Courage", "vibrasi": "Energi Kreatif",
        "blueprint": "Pencipta & Ekspresif. Anda membawa keindahan dan keceriaan ke dunia.",
        "hobi": "Seni Visual.", "hewan": "Kucing Lincah.", "karir": "Desainer/Artis."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "vibrasi": "Energi Logika",
        "blueprint": "Pemikir & Analitis. Anda adalah sumber solusi dan pengetahuan.",
        "hobi": "Catur/Coding.", "hewan": "Burung Beo.", "karir": "Programmer/Ilmuwan."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "state": "Reason", "vibrasi": "Energi Harmoni",
        "blueprint": "Penyembuh & Penyeimbang. Kehadiran Anda menenangkan lingkungan sekitar.",
        "hobi": "Berkebun.", "hewan": "Ikan Hias.", "karir": "Dokter/Arsitek."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "state": "Love", "vibrasi": "Energi Air",
        "blueprint": "Komunikator & Damai. Anda mampu menyatukan hati melalui kata-kata.",
        "hobi": "Bernyanyi.", "hewan": "Golden Retriever.", "karir": "Diplomat/Guru."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "state": "Joy", "vibrasi": "Energi Intuisi",
        "blueprint": "Visioner & Intuitif. Anda melihat masa depan yang tidak dilihat orang lain.",
        "hobi": "Astronomi.", "hewan": "Kucing Siam.", "karir": "Inovator."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "state": "Peace", "vibrasi": "Energi Spiritual",
        "blueprint": "Bijaksana & Inovatif. Anda adalah cahaya bagi perubahan besar.",
        "hobi": "Yoga/Filsafat.", "hewan": "Ikan Koi.", "karir": "Visioner/Artis."
    }
}

# --- 1. IDENTIFIKASI ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Silahkan masukkan nama anda:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=9)

if nama:
    st.divider()
    # --- 2. SCAN ---
    foto = st.camera_input("2. Scan Jati Diri & Aura")

    if foto:
        with st.status("🧬 Mengunduh Blue Print Jiwa...", expanded=False):
            time.sleep(1.5)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            warna_hasil = list(AURA_DB.keys())[int(brightness % 7)]
            res = AURA_DB[warna_hasil]
        
        # --- 4. HASIL ---
        st.subheader(f"Hasil Analisis Aura: {warna_hasil}")
        # Efek Visual
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        st.image(visual, caption=f"Blueprint Energy: {nama}")
        
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- BLUEPRINT PENGGUNA ---
        st.markdown(f"""
        <div class="blueprint-card">
        <h3 style='color:#FFD700; margin-top:0;'>🧬 My Life Blueprint</h3>
        <p><b>Vibrasi Utama:</b> {res['vibrasi']}</p>
        <p><b>Jati Diri:</b> {res['blueprint']}</p>
        </div>
        """, unsafe_allow_html=True)

        # --- GAYA HIDUP & REKOMENDASI ---
        st.divider()
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"🌿 *Hobi & Alam*\n\nHobi: {res['hobi']}\n\nHewan: {res['hewan']}")
        with col_b:
            if umur <= 18:
                st.success(f"📚 *Rekomendasi Belajar*\n\nFokus: {res['karir']}")
            else:
                st.success(f"💼 *Rekomendasi Karir*\n\nJalur: {res['karir']}")

    # --- COPYRIGHT FOOTER ---
    st.markdown(f"""
    <div class="copyright-text">
    © 2026 <b>Namikor</b>. All Rights Reserved.<br>
    AuraLens Pro Max AI - Official Version 4.0
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("Sistem Standby. Silahkan masukkan nama.")
