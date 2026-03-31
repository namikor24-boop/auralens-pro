import streamlit as st
from PIL import Image, ImageOps, ImageEnhance

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro")

# Database Warna & Saran
AURA_DATABASE = {
    "Merah": {"hex": "#FF0000", "desc": "Energi Berani & Semangat!", "karir": "Atlet, Sales, atau Pemimpin Lapangan."},
    "Emas": {"hex": "#FFD700", "desc": "Energi Bijak & Sukses!", "karir": "CEO, Mentor, atau Pengusaha."},
    "Cyan": {"hex": "#00FFFF", "desc": "Energi Damai & Komunikasi!", "karir": "Guru, HRD, atau Tenaga Medis."},
    "Ungu": {"hex": "#800080", "desc": "Energi Kreatif & Intuisi!", "karir": "Desainer, Artis, atau Penulis."}
}

# --- Langkah 1: Silahkan Tulis Nama ---
nama = st.text_input("1. Silahkan tulis nama kamu:", placeholder="Contoh: Mbak Ayi")

if nama:
    # --- Langkah 2: Pilih Warna & Mulai Scan ---
    st.divider()
    st.write(f"Halo *{nama}*, pilih warna aura yang ingin kamu scan:")
    pilihan = st.selectbox("2. Pilih warna aura visual:", list(AURA_DATABASE.keys()))
    
    # --- Langkah 3: Take Foto ---
    st.write("3. Ambil foto kamu untuk melihat energi aura:")
    foto = st.camera_input("Klik tombol di bawah untuk ambil foto")

    if foto:
        # PROSES VISUAL AURA
        img = Image.open(foto)
        img = ImageOps.exif_transpose(img) # Agar foto tidak miring
        
        # Membuat Efek Warna Aura
        warna_hex = AURA_DATABASE[pilihan]["hex"]
        rgb_color = tuple(int(warna_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        overlay = Image.new("RGB", img.size, rgb_color)
        hasil_img = Image.blend(img, overlay, alpha=0.3) # Pendaran aura 30%
        
        # --- Langkah 4: Hasil Foto Menampilkan Warna Aura ---
        st.divider()
        st.subheader("4. Hasil Foto Aura Kamu")
        st.image(hasil_img, caption=f"Aura {pilihan} terdeteksi pada {nama}")
        st.balloons()

        # --- Langkah 5 & 6: Deskripsi & Saran Karir ---
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            st.warning("✨ *5. Deskripsi Warna Aura*")
            st.write(AURA_DATABASE[pilihan]["desc"])
            
        with col2:
            st.success("💼 *6. Saran Karir*")
            st.write(AURA_DATABASE[pilihan]["karir"])

else:
    st.info("Ayo masukkan namamu di atas untuk memulai petualangan aura!")
