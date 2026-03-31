import streamlit as st
from PIL import Image, ImageOps, ImageEnhance

st.set_page_config(page_title="AuraLens Pro", page_icon="🔮")
st.title("🔮 AuraLens Pro: AI Visualizer")

# Database Warna & Deskripsi
AURA_MAP = {
    "Merah": {"warna": "#FF0000", "desc": "Energi Berani & Semangat tinggi!"},
    "Emas": {"warna": "#FFD700", "desc": "Energi Kelimpahan & Kepemimpinan!"},
    "Cyan": {"warna": "#00FFFF", "desc": "Energi Ketenangan & Komunikasi!"},
    "Ungu": {"warna": "#800080", "desc": "Energi Kreativitas & Intuisi!"}
}

with st.sidebar:
    st.header("Konfigurasi")
    nama = st.text_input("Nama Lengkap", value="Mbak Ayi")
    warna_pilihan = st.selectbox("Pilih Aura:", list(AURA_MAP.keys()))
    scan_tombol = st.button("Aktifkan Sensor Aura")

if scan_tombol:
    st.write(f"### Halo {nama}, Sensor sedang membaca energimu...")
    foto = st.camera_input("Ambil foto untuk melihat auramu")
    
    if foto:
        # PROSES EFEK VISUAL AURA
        img = Image.open(foto)
        
        # Membuat pendaran warna (tint)
        color = AURA_MAP[warna_pilihan]["warna"]
        aura_overlay = Image.new("RGB", img.size, color)
        combined = Image.blend(img, aura_overlay, alpha=0.3) # Efek transparan 30%
        
        # Meningkatkan kecerahan agar glowing
        enhancer = ImageEnhance.Brightness(combined)
        glowing_img = enhancer.enhance(1.2)
        
        st.image(glowing_img, caption=f"Visualisasi Aura {warna_pilihan} - {nama}")
        st.success(f"*Hasil Analisis:* {AURA_MAP[warna_pilihan]['desc']}")
        st.balloons()
else:
    st.info("Klik 'Aktifkan Sensor Aura' di samping untuk memulai.")
