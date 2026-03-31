import streamlit as st
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
    .spectrum-bar { height: 15px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin: 10px 0; }
    .lifestyle-card { background-color: #1E1E1E; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Lifestyle AI")
st.caption("“Analisis Bio-Energi Lengkap: Hobi, Aktivitas, hingga Hewan Peliharaan.”")

# Database Aura Terintegrasi
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Action",
        "hobi": "Olahraga bela diri, Gym, Balapan.",
        "aktivitas": "Hiking atau kompetisi fisik.",
        "tanaman": "Bunga Mawar Merah atau Cabai.",
        "hewan": "Anjing Penjaga (German Shepherd).",
        "belajar": "Kepemimpinan & Teknik.", "karir": "Atlet, Tentara, CEO."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "state": "Courage",
        "hobi": "Fotografi, Masak, Menari.",
        "aktivitas": "Membuat konten kreatif atau DIY.",
        "tanaman": "Bunga Matahari atau Marigold.",
        "hewan": "Kucing Oranye (Tabby) yang ceria.",
        "belajar": "Seni & Video Editing.", "karir": "Animator, Creator, Artis."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "state": "Willingness",
        "hobi": "Main catur, Membaca, Puzzle.",
        "aktivitas": "Belajar hal baru atau diskusi.",
        "tanaman": "Lemon atau Lidah Buaya.",
        "hewan": "Burung Beo atau Kenari.",
        "belajar": "Python Coding & Sains.", "karir": "Programmer, Ilmuwan, Dosen."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "state": "Reason",
        "hobi": "Berkebun, Yoga, Relawan.",
        "aktivitas": "Jalan-jalan di hutan/taman.",
        "tanaman": "Pohon Monstera atau Anggrek.",
        "hewan": "Kura-kura atau Ikan Hias.",
        "belajar": "Biologi & Psikologi.", "karir": "Dokter, Terapis, Arsitek."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "state": "Love",
        "hobi": "Bernyanyi, Menulis, Meditasi.",
        "aktivitas": "Public speaking atau berbagi cerita.",
        "tanaman": "Bunga Telang atau Lavender.",
        "hewan": "Anjing Golden Retriever yang setia.",
        "belajar": "Bahasa Asing & Sastra.", "karir": "Diplomat, Guru, PR."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "state": "Joy",
        "hobi": "Astronomi, Melukis, Game Strategi.",
        "aktivitas": "Mengamati bintang atau desain.",
        "tanaman": "Bunga Iris atau Violet.",
        "hewan": "Kucing Persia atau Siam.",
        "belajar": "Desain Masa Depan & Arsitektur.", "karir": "Product Designer, Inovator."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "state": "Peace",
        "hobi": "Filsafat, Seni Murni, Koleksi Batu Mulia.",
        "aktivitas": "Retreat spiritual atau riset AI.",
        "tanaman": "Pohon Bodhi atau Teratai.",
        "hewan": "Ikan Koi Putih atau Kucing Putih.",
        "belajar": "Quantum Physics & Seni.", "karir": "Visioner Tech, Founder."
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
    st.write(f"Halo *{nama}*, AI sedang menyiapkan pembacaan energi...")
    foto = st.camera_input("2. Ambil Foto Biometrik")

    if foto:
        # --- 3. PROSES AI ---
        with st.status("🔮 Menghitung Vektor Bio-Energi...", expanded=True) as status:
            time.sleep(1)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            vibrasi = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            idx = int(vibrasi % len(warna_keys))
            warna_hasil = warna_keys[idx]
            data = AURA_DB[warna_hasil]
            status.update(label="Analisis Gaya Hidup Selesai!", state="complete", expanded=False)
        
        # VISUALISASI
        color_rgb = tuple(int(data["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, color_rgb)
        visual = Image.blend(img, glow, alpha=0.25)
        
        # --- 4. HASIL ---
        st.divider()
        st.subheader(f"4. Analisis Aura: {warna_hasil}")
        st.image(visual, caption=f"Scan: {nama} | {time.strftime('%H:%M:%S')} WIB")
        
        st.markdown(f'<div class="hawkins-box">{data["hawkins"]} Log | {data["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- 5. DESKRIPSI & GAYA HIDUP (FITUR BARU) ---
        st.warning(f"✨ *5. Deskripsi & Gaya Hidup Aura {warna_hasil}*")
        col_la, col_lb = st.columns(2)
        with col_la:
            st.markdown(f"""
            <div class="lifestyle-card">
            <b>🎨 Hobi:</b> {data['hobi']}<br>
            <b>🏃 Aktivitas:</b> {data['aktivitas']}
            </div>
            """, unsafe_allow_html=True)
        with col_lb:
            st.markdown(f"""
            <div class="lifestyle-card">
            <b>🌿 Tanaman:</b> {data['tanaman']}<br>
            <b>🐾 Hewan:</b> {data['hewan']}
            </div>
            """, unsafe_allow_html=True)

        # --- 6. REKOMENDASI KARIR ---
        st.divider()
        if 7 <= umur <= 18:
            st.success(f"📚 *6. Rekomendasi Belajar (Usia {umur})*")
            st.write(f"Fokus belajar: *{data['belajar']}*")
        else:
            st.success(f"💼 *6. Rekomendasi Karir (Usia {umur})*")
            st.write(f"Jalur profesional: *{data['karir']}*")
else:
    st.info("Sistem Standby. Silahkan masukkan nama dan umur.")
