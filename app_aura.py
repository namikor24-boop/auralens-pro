import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import random
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro AI", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro: Auto AI Scanner")

# Database 7 Warna Pelangi & Saran
AURA_DB = {
    "Merah": {"hex": "#FF0000", "desc": "Energi Berani & Semangat!", "karir": "Atlet, Pemimpin, atau Sales."},
    "Jingga": {"hex": "#FF7F00", "desc": "Energi Kreatif & Ceria!", "karir": "Pemasaran, Seni, atau Animator."},
    "Kuning": {"hex": "#FFFF00", "desc": "Energi Optimis & Cerdas!", "karir": "Ilmuwan, Pengajar, atau Penulis."},
    "Hijau": {"hex": "#00FF00", "desc": "Energi Harmoni & Penyembuh!", "karir": "Dokter, Aktivis Lingkungan, atau Psikolog."},
    "Biru": {"hex": "#0000FF", "desc": "Energi Tenang & Komunikasi!", "karir": "Penyiar, HRD, atau Diplomat."},
    "Nila": {"hex": "#4B0082", "desc": "Energi Intuisi & Dalam!", "karir": "Desainer, Peneliti, atau Filosof."},
    "Ungu": {"hex": "#800080", "desc": "Energi Magis & Inovatif!", "karir": "Inovator Tech, Artis, atau Sutradara."}
}

# --- Langkah 1: Silahkan Tulis Nama ---
nama = st.text_input("1. Silahkan tulis nama kamu:", placeholder="Contoh: Mbak Ayi")

if nama:
    st.divider()
    # --- Langkah 2: Take Foto ---
    st.write(f"Halo *{nama}*, siapkan pose terbaikmu untuk scan AI.")
    foto = st.camera_input("2. Ambil foto kamu untuk mulai scan")

    if foto:
        # --- Langkah 3: Aplikasi Secara Otomatis Menscan ---
        with st.status("3. AI sedang menganalisis getaran aura...", expanded=True) as status:
            st.write("Mencari titik wajah...")
            time.sleep(1)
            st.write("Menghitung frekuensi warna...")
            time.sleep(1)
            # Pilih warna secara otomatis
            warna_hasil = random.choice(list(AURA_DB.keys()))
            status.update(label=f"Scan Selesai! Aura {warna_hasil} terdeteksi.", state="complete", expanded=False)
        
        # PROSES VISUAL AURA
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        
        warna_hex = AURA_DB[warna_hasil]["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- Langkah 4: Hasil Foto Menampilkan Warna Aura ---
        st.divider()
        st.subheader(f"4. Hasil Foto Aura {warna_hasil}")
        st.image(hasil_img, caption=f"Aura {warna_hasil} {nama} berhasil terdeteksi oleh AI")
        st.balloons()

        # --- Langkah 5 & 6: Deskripsi & Saran Karir ---
        col1, col2 = st.columns(2)
        with col1:
            st.warning(f"✨ *5. Deskripsi Aura {warna_hasil}*")
            st.write(AURA_DB[warna_hasil]["desc"])
            
        with col2:
            st.success("💼 *6. Saran Karir*")
            st.write(AURA_DB[warna_hasil]["karir"])
else:
    st.info("Tulis namamu dulu ya untuk mengaktifkan sensor AI!")
