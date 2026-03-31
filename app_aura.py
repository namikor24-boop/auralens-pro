import streamlit as st
from PIL import Image, ImageOps
import random
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro")
st.caption("“Energi Anda unik, dan aura Anda bisa berubah setiap detik.”")

# Database 7 Warna
AURA_DB = {
    "Merah": {"hex": "#FF0000", "desc": "Energi Berani & Semangat!", "karir": "Atlet atau Pemimpin."},
    "Jingga": {"hex": "#FF7F00", "desc": "Energi Kreatif & Ceria!", "karir": "Seni atau Pemasaran."},
    "Kuning": {"hex": "#FFFF00", "desc": "Energi Optimis & Cerdas!", "karir": "Guru atau Penulis."},
    "Hijau": {"hex": "#00FF00", "desc": "Energi Harmoni!", "karir": "Dokter atau Psikolog."},
    "Biru": {"hex": "#0000FF", "desc": "Energi Tenang!", "karir": "Diplomat atau HRD."},
    "Nila": {"hex": "#4B0082", "desc": "Energi Intuisi!", "karir": "Peneliti atau Desainer."},
    "Ungu": {"hex": "#800080", "desc": "Energi Inovatif!", "karir": "Artis atau Inovator."}
}

# --- Langkah 1: Tulis Nama ---
nama = st.text_input("1. Silahkan tulis nama kamu:", placeholder="Contoh: Mbak Ayi")

if nama:
    st.divider()
    # --- Langkah 2: Take Foto ---
    st.write(f"Halo *{nama}*, pancarkan energimu sekarang...")
    foto = st.camera_input("2. Ambil foto untuk scan detik ini")

    if foto:
        # LOGIKA SESUAI SLOGAN: Warna dipilih acak setiap kali foto diambil
        # Kita simpan di session_state supaya tidak berubah saat scrolling
        if 'warna_sekarang' not in st.session_state or st.button("🔄 Rescan Aura"):
            st.session_state.warna_sekarang = random.choice(list(AURA_DB.keys()))

        warna_hasil = st.session_state.warna_sekarang
        
        # --- Langkah 3: Animasi Scan ---
        with st.status("3. AI sedang membaca frekuensi energi...", expanded=False) as status:
            time.sleep(1)
            status.update(label=f"Terdeteksi! Aura kamu detik ini adalah {warna_hasil}.", state="complete")
        
        # PROSES VISUAL
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img)
        warna_hex = AURA_DB[warna_hasil]["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3)
        
        # --- Langkah 4: Hasil Foto ---
        st.divider()
        st.subheader(f"4. Visualisasi Aura {warna_hasil}")
        st.image(hasil_img, caption=f"Energi {nama} pada {time.strftime('%H:%M:%S')} WIB")
        st.balloons()

        # --- Langkah 5 & 6: Deskripsi & Karir ---
        col1, col2 = st.columns(2)
        with col1:
            st.warning(f"✨ *5. Arti Aura {warna_hasil}*")
            st.write(AURA_DB[warna_hasil]["desc"])
        with col2:
            st.success("💼 *6. Saran Karir*")
            st.write(AURA_DB[warna_hasil]["karir"])
            
        st.info("💡 Ingin lihat perubahan energimu? Silakan ambil foto lagi!")
else:
    st.info("Masukkan nama untuk memulai scan.")
