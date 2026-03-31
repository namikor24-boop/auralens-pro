import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Biometric", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 10px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #4B0082; }
    
    .spectrum-bar {
        height: 30px;
        width: 100%;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        border-radius: 15px;
        margin: 10px 0;
    }
    .score-box {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4B0082;
        background-color: white;
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Biometric AI")
st.caption("“Membaca frekuensi dan intensitas energi Anda.”")

AURA_DB = {
    "Merah": {"hex": "#FF0000", "desc": "Energi Berani & Vitalitas.", "karir": "Pemimpin, Atlet, atau Pengusaha."},
    "Jingga": {"hex": "#FF7F00", "desc": "Energi Kreatif & Ekspresif.", "karir": "Artis, Animator, atau Marketing."},
    "Kuning": {"hex": "#FFFF00", "desc": "Energi Intelek & Optimis.", "karir": "Ilmuwan, Guru, atau Penulis."},
    "Hijau": {"hex": "#00FF00", "desc": "Energi Keseimbangan & Alam.", "karir": "Dokter, Terapis, atau Arsitek."},
    "Biru": {"hex": "#0000FF", "desc": "Energi Tenang & Otoritas.", "karir": "Diplomat, HRD, atau Hukum."},
    "Nila": {"hex": "#4B0082", "desc": "Energi Intuisi & Spiritual.", "karir": "Psikolog, Peneliti, atau Desainer."},
    "Ungu": {"hex": "#800080", "desc": "Energi Inovatif & Magis.", "karir": "Sutradara, Artis, atau Inovator Tech."}
}

# --- 1. MASUKKAN NAMA ---
nama = st.text_input("1. Silahkan masukkan nama anda:", placeholder="Contoh: Rocky")

if nama:
    st.divider()
    # --- 2. TAKE FOTO ---
    st.write(f"Halo *{nama}*, sensor sedang menyiapkan pemindaian biometrik.")
    foto = st.camera_input("2. Ambil Foto Aura Detik Ini")

    if foto:
        # --- 3. PROSES SCAN ---
        with st.status("3. Menganalisis Intensitas Aura...", expanded=True) as status:
            st.write("🔍 Membaca data piksel wajah...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # LOGIKA ANGKA: Menghitung tingkat intensitas (0-100) berdasarkan cahaya
            img = Image.open(foto)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            # Menghasilkan skor angka antara 60-99 agar terlihat bagus
            skor_intensitas = int((brightness % 40) + 60)
            
            warna_keys = list(AURA_DB.keys())
            index_warna = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[index_warna]
            
            status.update(label=f"Analisis Selesai!", state="complete", expanded=False)
        
        # VISUALISASI
        img = ImageOps.exif_transpose(img)
        warna_hex = AURA_DB[warna_hasil]["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- 4. HASIL FOTO & SKOR ANGKA ---
        st.divider()
        st.subheader(f"4. Visualisasi Aura: {warna_hasil}")
        st.image(hasil_img, caption=f"Data Visual Aura {nama}")
        
        # Menampilkan Skor Angka
        st.write("📊 *Skor Intensitas Energi Anda:*")
        st.markdown(f'<div class="score-box">{skor_intensitas}%</div>', unsafe_allow_html=True)
        
        st.write("🌌 Pita Spektrum Energi:")
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)
        st.divider()

        # --- 5 & 6. DESKRIPSI & SARAN ---
        col1, col2 = st.columns(2)
        with col1:
            st.warning(f"✨ *5. Karakter Aura {warna_hasil}*")
            st.write(AURA_DB[warna_hasil]["desc"])
        with col2:
            st.success("💼 *6. Rekomendasi Karir*")
            st.write(AURA_DB[warna_hasil]["karir"])
else:
    st.info("Sistem Standby. Silahkan masukkan nama.")
