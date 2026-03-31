import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Biometric", page_icon="🔮")

# Gaya Tampilan agar Fokus ke Kamera & Spektrum
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 10px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #4B0082; }
    
    /* Gaya untuk Spektrum Warna yang Elegan */
    .spectrum-bar {
        height: 30px;
        width: 100%;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(75, 0, 130, 0.5); /* Glowing effect */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Biometric AI")
st.caption("“Membaca frekuensi energi Anda melalui sensor biometrik visual.”")

# Database 7 Warna Aura
AURA_DB = {
    "Merah": {"hex": "#FF0000", "desc": "Energi Berani & Vitalitas.", "karir": "Pemimpin, Atlet, atau Pengusaha."},
    "Jingga": {"hex": "#FF7F00", "desc": "Energi Kreatif & Ekspresif.", "karir": "Artis, Animator, atau Marketing."},
    "Kuning": {"hex": "#FFFF00", "desc": "Energi Intelek & Optimis.", "karir": "Ilmuwan, Guru, atau Penulis."},
    "Hijau": {"hex": "#00FF00", "desc": "Energi Keseimbangan & Alam.", "karir": "Dokter, Terapis, atau Arsitek."},
    "Biru": {"hex": "#0000FF", "desc": "Energi Tenang & Otoritas.", "karir": "Diplomat, HRD, atau Hukum."},
    "Nila": {"hex": "#4B0082", "desc": "Energi Intuisi & Spiritual.", "karir": "Psikolog, Peneliti, atau Desainer."},
    "Ungu": {"hex": "#800080", "desc": "Energi Inovatif & Magis.", "karir": "Sutradara, Artis, atau Inovator Tech."}
}

# --- LANGKAH 1: IDENTIFIKASI NAMA ---
nama = st.text_input("1. Masukkan Nama Pengguna:", placeholder="Contoh: Rocky")

if nama:
    st.divider()
    # --- LANGKAH 2: PENGAMBILAN DATA VISUAL ---
    st.write(f"Halo *{nama}*, sensor biometrik siap memindai energimu.")
    foto = st.camera_input("2. Ambil Foto Aura Detik Ini")

    if foto:
        # --- LANGKAH 3: SIMULASI SCAN REALISTIS ---
        with st.status("3. Memproses Analisis Aura...", expanded=True) as status:
            st.write("🔍 Memindai koordinat cahaya wajah...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01) # Animasi cepat
                progress_bar.progress(i + 1)
            
            # LOGIKA REALISTIS: Menentukan warna berdasarkan tingkat cahaya foto
            img = Image.open(foto)
            stat = ImageStat.Stat(img)
            brightness = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            index_warna = int(brightness % len(warna_keys))
            warna_hasil = warna_keys[index_warna]
            
            st.write(f"⚡ Frekuensi Terdeteksi: {round(brightness, 1)} Hz")
            status.update(label=f"Scan Berhasil! Aura {warna_hasil} Teridentifikasi.", state="complete", expanded=False)
        
        # PROSES VISUALISASI
        img = ImageOps.exif_transpose(img)
        warna_hex = AURA_DB[warna_hasil]["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- LANGKAH 4: DISPLAY HASIL & SPEKTRUM ---
        st.divider()
        st.subheader(f"4. Visualisasi Aura: {warna_hasil}")
        st.image(hasil_img, caption=f"Data Visual Aura {nama} - {time.strftime('%H:%M:%S')} WIB")
        
        # --- GANTI BALON DENGAN SPEKTRUM WARNA (Sesuai Gambar!) ---
        st.write("🌌 Energi Anda Terintegrasi dengan Spektrum Alam:")
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)
        st.divider()

        # --- LANGKAH 5 & 6: DESKRIPSI & SARAN LENGKAP ---
        col1, col2 = st.columns(2)
        with col1:
            st.warning(f"✨ *5. Karakter Aura {warna_hasil}*")
            st.write(AURA_DB[warna_hasil]["desc"])
        with col2:
            st.success("💼 *6. Rekomendasi Karir*")
            st.write(AURA_DB[warna_hasil]["karir"])
            
        st.info("💡 Aura bersifat dinamis. Perubahan cahaya atau ekspresi dapat mempengaruhi hasil scan berikutnya.")
else:
    st.info("Sistem standby. Masukkan nama untuk mengaktifkan sensor.")
