import streamlit as st

# Konfigurasi Halaman Dasar
st.set_page_config(page_title="AuraLens Pro", page_icon="🔮")

st.title("🔮 AuraLens Pro: AI Scanner")

# Data Aura yang Sederhana (Anti-Error)
AURA_DATABASE = {
    "Merah": "Energi Berani - Cocok di bidang Sales/Atlet.",
    "Emas": "Energi Pemimpin - Cocok jadi CEO/Mentor.",
    "Cyan": "Energi Damai - Cocok jadi Guru/Konselor.",
    "Ungu": "Energi Kreatif - Cocok jadi Desainer/Artis."
}

# Sidebar untuk Input
with st.sidebar:
    st.header("Konfigurasi")
    nama = st.text_input("Nama Lengkap", "")
    warna_pilihan = st.selectbox("Pilih Aura:", list(AURA_DATABASE.keys()))
    tombol_scan = st.button("Mulai Scan Sekarang")

# Logika Utama
if nama:
    st.write(f"### Halo, {nama}!")
    
    if tombol_scan:
        st.success(f"Hasil Scan: Aura {warna_pilihan}")
        st.write(f"*Analisis Karir:* {AURA_DATABASE[warna_pilihan]}")
        
        # Fitur Ambil Foto (Paling Stabil di HP)
        st.info("Ambil foto untuk melihat visualisasi auramu:")
        foto = st.camera_input("Klik tombol di bawah untuk foto")
        
        if foto:
            st.image(foto, caption=f"Aura {warna_pilihan} terdeteksi!")
            st.balloons()
    else:
        st.info("Silakan klik tombol 'Mulai Scan Sekarang' di samping.")
else:
    st.warning("Masukkan nama kamu di kolom sebelah kiri dulu ya!")
