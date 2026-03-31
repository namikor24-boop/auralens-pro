[18.05, 31/3/2026] ROKIMAN: import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Lifestyle AI", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 12px; font-weight: bold; border: 2px solid #FFD700; }
    .hawkins-box {
        font-size: 30px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 15px; border: 2px solid #FFD700;
    }
    .spectrum-bar { height: 15px; width: 100%; background: linear-gradient(to right, red, orange…
[18.06, 31/3/2026] ROKIMAN: https://auralens-pro-namikor.streamlit.app/
[18.14, 31/3/2026] ROKIMAN: import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Lifestyle AI", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 12px; font-weight: bold; border: 2px solid #FFD700; }
    .hawkins-box {
        font-size: 28px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 15px; border: 2px solid #FFD700;
    }
    .spectrum-bar { height: 15px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin: 10px 0; }
    .lifestyle-card { background-color: #1E1E1E; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 10px; font-size: 14px; }
    .energy-label { color: #FFD700; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Lifestyle AI")
st.caption("“Analisis Gaya Hidup Berdasarkan Spektrum Energi Biometrik.”")

# Database Aura dengan Analisis Energi yang Akurat
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "vibrasi": "Energi Api (Ekspansif)",
        "hobi": "Bela diri atau olahraga intensitas tinggi untuk menyalurkan energi panas.",
        "aktivitas": "Kompetisi atau tantangan fisik yang memacu adrenalin.",
        "tanaman": "Tanaman berduri atau berwarna tajam seperti Kaktus atau Mawar Merah.",
        "hewan": "Anjing yang aktif dan protektif seperti Doberman atau Rottweiler.",
        "belajar": "Kepemimpinan Strategis.", "karir": "Manajer Operasional atau Atlet."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "vibrasi": "Energi Kreatif (Mengalir)",
        "hobi": "Memasak atau kerajinan tangan untuk mengolah ide menjadi benda nyata.",
        "aktivitas": "Menari atau bersosialisasi di tempat yang penuh warna.",
        "tanaman": "Tanaman buah yang produktif seperti Pohon Jeruk atau Tomat.",
        "hewan": "Hewan yang lincah dan ceria seperti Kucing Tabby atau Hamster.",
        "belajar": "Seni Visual & Desain.", "karir": "Content Creator atau Desainer Produk."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "vibrasi": "Energi Cahaya (Intelektual)",
        "hobi": "Catur, teka-teki silang, atau coding untuk menstimulasi logika.",
        "aktivitas": "Membaca buku non-fiksi atau berdiskusi tentang ide-ide baru.",
        "tanaman": "Tanaman herbal yang bermanfaat seperti Mint atau Lidah Buaya.",
        "hewan": "Burung yang cerdas dan komunikatif seperti Beo atau Kakaktua.",
        "belajar": "Sains & Teknologi (AI).", "karir": "Analyst, Programmer, atau Peneliti."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "vibrasi": "Energi Pertumbuhan (Harmoni)",
        "hobi": "Berkebun atau fotografi alam untuk menyatu dengan frekuensi bumi.",
        "aktivitas": "Earthing (berjalan tanpa alas kaki di rumput) atau Meditasi Alam.",
        "tanaman": "Tanaman berdaun lebar yang menenangkan seperti Monstera atau Paku-pakuan.",
        "hewan": "Hewan yang tenang dan stabil seperti Kura-kura atau Ikan Hias.",
        "belajar": "Ilmu Kesehatan & Ekologi.", "karir": "Dokter, Terapis, atau Arsitek Hijau."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "vibrasi": "Energi Air (Kedamaian)",
        "hobi": "Bernyanyi, menulis jurnal, atau berenang untuk menenangkan pikiran.",
        "aktivitas": "Mendengarkan musik instrumen atau berbicara di depan umum.",
        "tanaman": "Tanaman air atau bunga berwarna biru seperti Lotus atau Hydrangea.",
        "hewan": "Anjing yang setia dan tenang seperti Golden Retriever atau Labrador.",
        "belajar": "Komunikasi & Sastra.", "karir": "Diplomat, Guru, atau Public Relations."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "vibrasi": "Energi Ruang (Intuisi)",
        "hobi": "Mengamati bintang (astronomi) atau melukis abstrak.",
        "aktivitas": "Latihan visualisasi atau eksplorasi tempat-tempat bersejarah.",
        "tanaman": "Tanaman yang unik dan langka seperti Bunga Anggrek Hitam.",
        "hewan": "Kucing yang mandiri dan misterius seperti Kucing Siam atau Hitam.",
        "belajar": "Inovasi Masa Depan.", "karir": "Trend Forecaster atau Inovator."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "vibrasi": "Energi Eterik (Spiritual)",
        "hobi": "Yoga tingkat tinggi, belajar filsafat, atau koleksi kristal.",
        "aktivitas": "Retreat kesunyian atau riset tentang teknologi masa depan.",
        "tanaman": "Tanaman yang dianggap suci atau simbolis seperti Bunga Teratai.",
        "hewan": "Hewan yang anggun dan langka seperti Ikan Koi Putih atau Kuda.",
        "belajar": "Quantum Physics & Metafisika.", "karir": "Visioner, Founder Startup, atau Artis."
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
    # --- 2. CAMERA AI ---
    st.write(f"Halo *{nama}*, mohon tenang, AI sedang memetakan spektrum energimu...")
    foto = st.camera_input("2. Scan Frekuensi Bio-Energi")

    if foto:
        # --- 3. PROSES AI ---
        with st.status("🧬 Menganalisis Kepadatan Energi...", expanded=True) as status:
            time.sleep(1)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            vibrasi = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            idx = int(vibrasi % len(warna_keys))
            warna_hasil = warna_keys[idx]
            data = AURA_DB[warna_hasil]
            status.update(label=f"Energi {warna_hasil} Teridentifikasi!", state="complete", expanded=False)
        
        # VISUALISASI
        color_rgb = tuple(int(data["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, color_rgb)
        visual = Image.blend(img, glow, alpha=0.25)
        
        # --- 4. HASIL ---
        st.divider()
        st.subheader(f"4. Hasil Scan: {warna_hasil}")
        st.image(visual, caption=f"Bio-Energy Mapping: {nama}")
        
        st.markdown(f'<div class="hawkins-box">{data["hawkins"]} Log | {data["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- 5. ANALISIS GAYA HIDUP BERBASIS ENERGI ---
        st.write(f"### 5. Analisis Gaya Hidup: {data['vibrasi']}")
        
        col_la, col_lb = st.columns(2)
        with col_la:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-label">🎨 Hobi & Aktivitas</span><br>
            <b>Hobi:</b> {data['hobi']}<br><br>
            <b>Aktivitas:</b> {data['aktivitas']}
            </div>
            """, unsafe_allow_html=True)
        with col_lb:
            st.markdown(f"""
            <div class="lifestyle-card">
            <span class="energy-label">🌿 Alam & Lingkungan</span><br>
            <b>Tanaman:</b> {data['tanaman']}<br><br>
            <b>Hewan Peliharaan:</b> {data['hewan']}
            </div>
            """, unsafe_allow_html=True)

        # --- 6. REKOMENDASI MASA DEPAN ---
        st.divider()
        if 7 <= umur <= 18:
            st.success(f"📚 *6. Rekomendasi Belajar (Usia {umur})*")
            st.write(f"Sesuai energi *{warna_hasil}, fokuslah pada: *{data['belajar']}**")
        else:
            st.success(f"💼 *6. Rekomendasi Karir (Usia {umur})*")
            st.write(f"Sesuai energi *{warna_hasil}, jalur terbaikmu: *{data['karir']}**")
            
        st.info("💡 *Tips:* Energi aura bisa berubah setiap detik. Lakukan aktivitas di atas untuk menjaga vibrasi Anda tetap tinggi.")
else:
    st.info("Sistem Standby. Silahkan masukkan data diri.")
