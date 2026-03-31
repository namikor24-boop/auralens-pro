import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro x Education", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 10px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #4B0082; }
    
    .spectrum-bar {
        height: 20px;
        width: 100%;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        border-radius: 10px;
        margin: 10px 0;
    }
    .hawkins-box {
        font-size: 35px;
        font-weight: bold;
        text-align: center;
        color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #8A2BE2);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border: 2px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Life Path AI")
st.caption("“Analisis Energi, Pendidikan, dan Karir berdasarkan Skala Hawkins.”")

# Database Aura & Skala Hawkins
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Anger/Semangat", 
        "desc": "Energi aksi dan keberanian fisik.", 
        "belajar": "Olahraga, Kepemimpinan, Teknik Mesin.",
        "karir": "Atlet Profesional, Tentara, Manajer Operasional."
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "state": "Courage/Keberanian", 
        "desc": "Energi kreativitas dan ekspresi diri.", 
        "belajar": "Seni Visual, Desain Grafis, Video Editing.",
        "karir": "Content Creator, Animator, Creative Director."
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "state": "Willingness/Kemauan", 
        "desc": "Energi optimisme dan logika cerdas.", 
        "belajar": "Matematika, Coding (Python), Sains.",
        "karir": "Data Scientist, Programmer, Dosen/Peneliti."
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "state": "Reason/Penerimaan", 
        "desc": "Energi harmoni dan penyembuhan.", 
        "belajar": "Biologi, Psikologi, Ilmu Lingkungan.",
        "karir": "Dokter, Konselor, Aktivis Lingkungan."
    },
    "Biru": {
        "hex": "#0000FF", "hawkins": 500, "state": "Love/Ketulusan", 
        "desc": "Energi komunikasi dan kedamaian.", 
        "belajar": "Bahasa Asing, Public Speaking, Sastra.",
        "karir": "Diplomat, Public Relations, Guru."
    },
    "Nila": {
        "hex": "#4B0082", "hawkins": 540, "state": "Joy/Kegembiraan", 
        "desc": "Energi intuisi dan visi masa depan.", 
        "belajar": "Desain UI/UX, Arsitektur, Astronomi.",
        "karir": "Product Designer, Inovator, Arsitek."
    },
    "Ungu": {
        "hex": "#800080", "hawkins": 600, "state": "Peace/Kedamaian", 
        "desc": "Energi spiritual dan inovasi radikal.", 
        "belajar": "Filsafat, Teknologi Masa Depan (AI), Seni Murni.",
        "karir": "Founder Startup, Artis, Visioner Tech."
    }
}

# --- LANGKAH 1: IDENTIFIKASI NAMA & UMUR ---
col_n, col_u = st.columns([3, 1])
with col_n:
    nama = st.text_input("1. Silahkan masukkan nama anda:", placeholder="Contoh: Rocky")
with col_u:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=19)

if nama:
    st.divider()
    # --- LANGKAH 2: TAKE FOTO ---
    st.write(f"Halo *{nama}* ({umur} thn), sensor biometrik siap mendeteksi jalur hidup Anda.")
    foto = st.camera_input("2. Ambil Foto Aura Detik Ini")

    if foto:
        # --- LANGKAH 3: PROSES SCAN ---
        with st.status("3. Menganalisis Frekuensi Biometrik...", expanded=True) as status:
            st.write("🔍 Menghitung vibrasi Hawkins...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            img = Image.open(foto)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            index_warna = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[index_warna]
            data = AURA_DB[warna_hasil]
            
            status.update(label="Analisis Bio-Energi Selesai!", state="complete", expanded=False)
        
        # VISUALISASI
        img = ImageOps.exif_transpose(img)
        warna_hex = data["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- LANGKAH 4: DISPLAY HASIL ---
        st.divider()
        st.subheader(f"4. Visualisasi Aura: {warna_hasil}")
        st.image(hasil_img, caption=f"Data Bio-Energi {nama} - {umur} Tahun")
        
        st.markdown(f'''
            <div class="hawkins-box">
                {data['hawkins']} Log<br>
                <span style="font-size: 18px;">Status: {data['state']}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)
        st.divider()

        # --- LANGKAH 5 & 6: DESKRIPSI & REKOMENDASI (LOGIKA UMUR) ---
        c1, c2 = st.columns(2)
        with c1:
            st.warning(f"✨ *5. Karakter Aura {warna_hasil}*")
            st.write(data["desc"])
        
        with c2:
            # LOGIKA UTAMA MBAK AYI: Membedakan Belajar vs Karir
            if 7 <= umur <= 18:
                st.success("📚 *6. Rekomendasi Belajar*")
                st.write(f"Untuk usia {umur} tahun, fokuslah mempelajari: *{data['belajar']}*")
            else:
                st.success("💼 *6. Rekomendasi Karir*")
                st.write(f"Untuk usia {umur} tahun, jalur karir terbaik adalah: *{data['karir']}*")
            
        st.info(f"💡 *Saran:* Gunakan energi {warna_hasil} Anda untuk memaksimalkan potensi di bidang tersebut.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama dan umur untuk memulai.")
