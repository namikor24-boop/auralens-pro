import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Lifestyle AI", page_icon="🔮")

# CSS Premium (Dibuat sangat simpel agar tidak bentrok dengan Python)
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
        margin: 10px 0px;
    }
    .spectrum-bar { 
        height: 15px; 
        width: 100%; 
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); 
        border-radius: 10px; 
        margin: 15px 0px; 
    }
    .lifestyle-card { 
        background-color: #1E1E1E; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #FFD700; 
        margin-bottom: 10px; 
    }
    .energy-tag { color: #FFD700; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Lifestyle AI")
st.caption("“Membaca frekuensi energi biometrik dan jalur hidup Anda.”")

# Database Aura & Analisis Gaya Hidup Berbasis Energi
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Action/Anger", "vibrasi": "Energi Api (Ekspansif)",
        "hobi": "Olahraga berat atau bela diri.", "aktivitas": "Tantangan fisik di alam terbuka.",
        "tanaman": "Mawar Merah atau Kaktus.", "hewan": "Anjing penjaga yang setia.",
        "belajar": "Leadership & Teknik.", "karir": "Atlet, CEO, atau Militer."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "state": "Courage", "vibrasi": "Energi Kreatif (Mengalir)",
        "hobi": "Memasak atau seni dekorasi.", "aktivitas": "Menari atau membuat video kreatif.",
        "tanaman": "Pohon Jeruk atau Bunga Matahari.", "hewan": "Kucing yang lincah.",
        "belajar": "Seni Visual & Desain.", "karir": "Animator atau Marketing."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "vibrasi": "Energi Cahaya (Intelektual)",
        "hobi": "Catur atau belajar coding.", "aktivitas": "Diskusi ide atau membaca buku sains.",
        "tanaman": "Lidah Buaya atau Mint.", "hewan": "Burung Beo yang cerdas.",
        "belajar": "Coding (Python) & Matematika.", "karir": "Programmer atau Analis."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "state": "Reason", "vibrasi": "Energi Pertumbuhan (Harmoni)",
        "hobi": "Berkebun atau fotografi alam.", "aktivitas": "Meditasi di bawah pohon.",
        "tanaman": "Monstera atau Anggrek Hijau.", "hewan": "Kura-kura atau Ikan Hias.",
        "belajar": "Biologi & Psikologi.", "karir": "Dokter atau Arsitek."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "state": "Love", "vibrasi": "Energi Air (Kedamaian)",
        "hobi": "Bernyanyi atau berenang.", "aktivitas": "Menulis jurnal atau relaksasi air.",
        "tanaman": "Hydrangea atau Teratai Biru.", "hewan": "Anjing Golden Retriever.",
        "belajar": "Bahasa Asing & Komunikasi.", "karir": "Diplomat atau Guru."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "state": "Joy", "vibrasi": "Energi Ruang (Intuisi)",
        "hobi": "Mengamati bintang (astronomi).", "aktivitas": "Latihan visualisasi atau meditasi.",
        "tanaman": "Bunga Iris atau Lavender.", "hewan": "Kucing Siam yang anggun.",
        "belajar": "Inovasi & Arsitektur.", "karir": "Trend Forecaster."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "state": "Peace", "vibrasi": "Energi Eterik (Spiritual)",
        "hobi": "Belajar filsafat atau yoga.", "aktivitas": "Riset teknologi masa depan.",
        "tanaman": "Bunga Teratai atau Bodhi.", "hewan": "Ikan Koi atau Kuda.",
        "belajar": "Quantum Physics & Seni.", "karir": "Visioner atau Artis."
    }
}

# --- 1. IDENTIFIKASI ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Silahkan masukkan nama anda:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=19)

if nama:
    st.divider()
    # --- 2. CAMERA AI ---
    st.write(f"Halo *{nama}*, mohon tunggu, AI sedang memindai biometrik wajah Anda...")
    foto = st.camera_input("2. Ambil Foto Aura")

    if foto:
        # --- 3. PROSES AI REALISTIS ---
        with st.status("🧬 Menganalisis Spektrum Energi...", expanded=False) as status:
            time.sleep(1)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            # Menghitung warna berdasarkan cahaya foto asli
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            idx = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[idx]
            res = AURA_DB[warna_hasil]
            status.update(label=f"Aura {warna_hasil} Terdeteksi!", state="complete")
        
        # VISUALISASI SIHIR AURA
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        
        # --- 4. HASIL FOTO & SKALA HAWKINS ---
        st.divider()
        st.subheader(f"4. Hasil Analisis Aura: {warna_hasil}")
        st.image(visual, caption=f"Bio-Energy Mapping: {nama}")
        
        # Box Hawkins yang Mewah
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | {res["state"]}</div>', unsafe_allow_html=True)
        # Spektrum Warna Pelangi (Sesuai gambar Mbak Ayi)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- 5. ANALISIS GAYA HIDUP BERBASIS ENERGI ---
        st.write(f"### 5. Analisis Gaya Hidup: {res['vibrasi']}")
        la, lb = st.columns(2)
        with la:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-tag">🎨 Hobi & Aktivitas</span><br>
            <b>Hobi:</b> {res['hobi']}<br>
            <b>Aktivitas:</b> {res['aktivitas']}
            </div>
            """, unsafe_allow_html=True)
        with lb:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-tag">🌿 Alam & Lingkungan</span><br>
            <b>Tanaman:</b> {res['tanaman']}<br>
            <b>Hewan:</b> {res['hewan']}
            </div>
            """, unsafe_allow_html=True)

        # --- 6. REKOMENDASI MASA DEPAN (LOGIKA UMUR) ---
        st.divider()
        if 7 <= umur <= 18:
            st.success(f"📚 *6. Rekomendasi Belajar (Usia {umur} thn)*")
            st.write(f"Sesuai vibrasi *{warna_hasil}, fokuslah mendalami: *{res['belajar']}**")
        else:
            st.success(f"💼 *6. Rekomendasi Karir (Usia {umur} thn)*")
            st.write(f"Sesuai vibrasi *{warna_hasil}, jalur karir terbaikmu: *{res['karir']}**")
else:
    st.info("Sistem Standby. Silahkan masukkan nama dan umur.")
