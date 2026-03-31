import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Lifestyle AI", page_icon="🔮")

# CSS untuk tampilan Premium (Menggunakan st.write dengan unsafe_allow_html agar aman dari KeyError)
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
        font-size: 28px; 
        font-weight: bold; 
        text-align: center; 
        color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; 
        padding: 15px; 
        border: 2px solid #FFD700;
    }
    .spectrum-bar { 
        height: 15px; 
        width: 100%; 
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); 
        border-radius: 10px; 
        margin: 10px 0; 
    }
    .lifestyle-card { 
        background-color: #1E1E1E; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #FFD700; 
        margin-bottom: 10px; 
    }
    .energy-label { color: #FFD700; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Lifestyle AI")
st.caption("Analisis Gaya Hidup & Energi Biometrik")

# Database Aura & Gaya Hidup
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "vibrasi": "Energi Api (Ekspansif)",
        "hobi": "Bela diri atau olahraga intensitas tinggi.",
        "aktivitas": "Hiking atau tantangan fisik yang memacu adrenalin.",
        "tanaman": "Kaktus atau Mawar Merah.",
        "hewan": "Anjing yang aktif (Doberman/Rottweiler).",
        "belajar": "Kepemimpinan Strategis.", "karir": "Manajer atau Atlet."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "vibrasi": "Energi Kreatif (Mengalir)",
        "hobi": "Memasak atau kerajinan tangan.",
        "aktivitas": "Menari atau membuat konten kreatif.",
        "tanaman": "Pohon Jeruk atau Tomat.",
        "hewan": "Kucing Tabby atau Hamster yang lincah.",
        "belajar": "Seni Visual & Desain.", "karir": "Content Creator atau Animator."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "vibrasi": "Energi Cahaya (Intelektual)",
        "hobi": "Catur, teka-teki, atau coding.",
        "aktivitas": "Membaca buku non-fiksi atau berdiskusi.",
        "tanaman": "Mint atau Lidah Buaya.",
        "hewan": "Burung Beo atau Kakaktua yang cerdas.",
        "belajar": "Sains & Teknologi (AI).", "karir": "Programmer atau Peneliti."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "vibrasi": "Energi Pertumbuhan (Harmoni)",
        "hobi": "Berkebun atau fotografi alam.",
        "aktivitas": "Meditasi di taman atau earthing.",
        "tanaman": "Monstera atau Paku-pakuan.",
        "hewan": "Kura-kura atau Ikan Hias.",
        "belajar": "Ilmu Kesehatan & Ekologi.", "karir": "Dokter atau Arsitek Hijau."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "vibrasi": "Energi Air (Kedamaian)",
        "hobi": "Bernyanyi, menulis jurnal, atau berenang.",
        "aktivitas": "Mendengarkan musik instrumen.",
        "tanaman": "Lotus atau Hydrangea.",
        "hewan": "Anjing Golden Retriever yang setia.",
        "belajar": "Komunikasi & Sastra.", "karir": "Diplomat atau Guru."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "vibrasi": "Energi Ruang (Intuisi)",
        "hobi": "Mengamati bintang (astronomi).",
        "aktivitas": "Latihan visualisasi atau meditasi dalam.",
        "tanaman": "Bunga Anggrek Hitam atau Iris.",
        "hewan": "Kucing Siam yang misterius.",
        "belajar": "Inovasi Masa Depan.", "karir": "Trend Forecaster atau Inovator."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "vibrasi": "Energi Eterik (Spiritual)",
        "hobi": "Yoga, belajar filsafat, atau koleksi kristal.",
        "aktivitas": "Retreat kesunyian.",
        "tanaman": "Bunga Teratai atau Pohon Bodhi.",
        "hewan": "Ikan Koi Putih atau Kuda.",
        "belajar": "Quantum Physics.", "karir": "Visioner atau Artis."
    }
}

# --- 1. IDENTIFIKASI ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=19)

if nama:
    st.divider()
    foto = st.camera_input("2. Ambil Foto Biometrik")

    if foto:
        with st.status("🧬 Menganalisis Kepadatan Energi...", expanded=False):
            time.sleep(1)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            idx = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[idx]
            data = AURA_DB[warna_hasil]
        
        # VISUALISASI
        color_rgb = tuple(int(data["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, color_rgb)
        visual = Image.blend(img, glow, alpha=0.25)
        
        # --- 4. HASIL ---
        st.divider()
        st.subheader(f"4. Hasil Analisis Aura: {warna_hasil}")
        st.image(visual, caption=f"Bio-Energy Mapping: {nama}")
        
        # Menggunakan format yang lebih aman untuk variabel di dalam HTML
        hawkins_val = data['hawkins']
        hawkins_state = data['state']
        st.markdown(f'<div class="hawkins-box">{hawkins_val} Log | {hawkins_state}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- 5. ANALISIS GAYA HIDUP ---
        st.write(f"### 5. Analisis Gaya Hidup: {data['vibrasi']}")
        col_la, col_lb = st.columns(2)
        with col_la:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-label">🎨 Hobi & Aktivitas</span><br>
            <b>Hobi:</b> {data['hobi']}<br>
            <b>Aktivitas:</b> {data['aktivitas']}
            </div>
            """, unsafe_allow_html=True)
        with col_lb:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-label">🌿 Alam & Lingkungan</span><br>
            <b>Tanaman:</b> {data['tanaman']}<br>
            <b>Hewan:</b> {data['hewan']}
            </div>
            """, unsafe_allow_html=True)

        # --- 6. REKOMENDASI ---
        st.divider()
        if 7 <= umur <= 18:
            st.success(f"📚 *6. Rekomendasi Belajar (Usia {umur} thn)*")
            st.write(f"Sesuai energi *{warna_hasil}, fokuslah pada: *{data['belajar']}**")
        else:
            st.success(f"💼 *6. Rekomendasi Karir (Usia {umur} thn)*")
            st.write(f"Sesuai energi *{warna_hasil}, jalur terbaikmu: *{data['karir']}**")
else:
    st.info("Sistem Standby. Silahkan masukkan data diri.")
