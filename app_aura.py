import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro x Hawkins", page_icon="🔮")

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

st.title("🔮 AuraLens Pro: Hawkins Energy AI")
st.caption("“Mengukur frekuensi kesadaran Anda berdasarkan Skala Hawkins.”")

# Database Aura dengan Hubungan Skala Hawkins
# Urutan: Merah (Bawah) ke Ungu (Tinggi)
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Anger/Semangat", "desc": "Energi aksi dan keberanian fisik.", "karir": "Atlet, Pemimpin Proyek."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage/Keberanian", "desc": "Titik balik energi positif dan kreativitas.", "karir": "Marketing, Animator."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness/Kemauan", "desc": "Energi optimisme dan kecerdasan logika.", "karir": "Guru, Ilmuwan."},
    "Hijau": {"hex": "#00FF00", "desc": "Energi keseimbangan dan penyembuhan.", "hawkins": 400, "state": "Reason/Penerimaan", "karir": "Dokter, Psikolog."},
    "Biru": {"hex": "#0000FF", "desc": "Energi kedamaian dan komunikasi.", "hawkins": 500, "state": "Love/Ketulusan", "karir": "Diplomat, HRD."},
    "Nila": {"hex": "#4B0082", "desc": "Energi intuisi dan visi dalam.", "hawkins": 540, "state": "Joy/Kegembiraan", "karir": "Desainer, Peneliti."},
    "Ungu": {"hex": "#800080", "desc": "Energi spiritual dan inovasi.", "hawkins": 600, "state": "Peace/Kedamaian", "karir": "Inovator Tech, Artis."}
}

# --- 1. IDENTIFIKASI ---
nama = st.text_input("1. Silahkan masukkan nama anda:", placeholder="Contoh: Rocky")

if nama:
    st.divider()
    # --- 2. TAKE FOTO ---
    st.write(f"Halo *{nama}*, sensor sedang menghubungkan frekuensi Anda ke Skala Hawkins...")
    foto = st.camera_input("2. Ambil Foto Biometrik")

    if foto:
        # --- 3. PROSES SCAN ---
        with st.status("3. Menganalisis Spektrum Kesadaran...", expanded=True) as status:
            st.write("🔍 Membaca vibrasi molekuler...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # Hitung warna berdasarkan cahaya foto
            img = Image.open(foto)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            index_warna = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[index_warna]
            data_aura = AURA_DB[warna_hasil]
            
            status.update(label="Analisis Hawkins Selesai!", state="complete", expanded=False)
        
        # VISUALISASI
        img = ImageOps.exif_transpose(img)
        warna_hex = data_aura["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- 4. HASIL FOTO & SKALA HAWKINS ---
        st.divider()
        st.subheader(f"4. Visualisasi Aura: {warna_hasil}")
        st.image(hasil_img, caption=f"Data Bio-Energi {nama}")
        
        st.write("📊 *Tingkat Kesadaran (Hawkins Scale):*")
        st.markdown(f'''
            <div class="hawkins-box">
                {data_aura['hawkins']} Log<br>
                <span style="font-size: 18px;">Status: {data_aura['state']}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)
        st.divider()

        # --- 5 & 6. DESKRIPSI & KARIR ---
        col1, col2 = st.columns(2)
        with col1:
            st.warning(f"✨ *5. Deskripsi Energi {warna_hasil}*")
            st.write(data_aura["desc"])
        with col2:
            st.success("💼 *6. Rekomendasi Karir*")
            st.write(data_aura["karir"])
            
        st.info(f"💡 *Info:* Dalam Skala Hawkins, angka {data_aura['hawkins']} menunjukkan tingkat vibrasi dominan Anda saat ini.")
else:
    st.info("Sistem Standby. Silahkan masukkan nama.")
