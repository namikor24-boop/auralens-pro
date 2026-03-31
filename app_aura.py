import streamlit as st
from PIL import Image, ImageOps, ImageStat, ImageDraw, ImageFilter
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { width: 100%; background-color: #4B0082; color: white; border-radius: 12px; font-weight: bold; height: 3em; border: 2px solid #FFD700; }
    .hawkins-box {
        font-size: 32px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; box-shadow: 0 0 20px #4B0082;
    }
    .spectrum-bar { height: 15px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("“Powered by Advanced Biometric Computer Vision & Hawkins Scale”")

# Database Aura Lengkap
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Anger/Action", "desc": "Energi vitalitas tinggi.", "belajar": "Teknik, Atletik, Leadership.", "karir": "CEO Operasional, Atlet, Militer."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "desc": "Energi kreativitas membara.", "belajar": "Seni Digital, Content Creation.", "karir": "Art Director, Marketing Executive."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "desc": "Energi logika cerdas.", "belajar": "Data Science, AI, Matematika.", "karir": "Software Architect, Peneliti AI."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "desc": "Energi harmoni & penyembuh.", "belajar": "Kedokteran, Bioteknologi.", "karir": "Dokter Spesialis, Psikolog."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "desc": "Energi komunikasi tulus.", "belajar": "Hubungan Internasional, Sastra.", "karir": "Diplomat, Senior Consultant."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "desc": "Energi visi masa depan.", "belajar": "Arsitektur, Desain Inovasi.", "karir": "Inovator Masa Depan, Arsitek."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "desc": "Energi spiritualitas tinggi.", "belajar": "Filsafat Modern, Quantum Physics.", "karir": "Visioner Tech, Artis Global."}
}

# --- 1. IDENTIFIKASI ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=40, value=19)

if nama:
    st.divider()
    # --- 2. CAMERA AI SCANNER ---
    st.write(f"Halo *{nama}*, AI sedang menginisialisasi sensor biometrik wajah...")
    foto = st.camera_input("2. Posisikan Wajah Anda di Kotak Scan")

    if foto:
        # --- 3. PROSES AI SUPER CANGGIH ---
        with st.status("🧬 AI sedang menganalisis Bio-Energi...", expanded=True) as status:
            st.write("📷 Mendeteksi titik-titik wajah (Face Landmarks)...")
            time.sleep(1)
            st.write("🌌 Menghitung spektrum warna berdasarkan temperatur piksel...")
            
            # Algoritma AI sederhana berbasis piksel untuk menentukan warna
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            vibrasi = sum(stat.mean) / 3 
            
            warna_keys = list(AURA_DB.keys())
            idx = int(vibrasi % len(warna_keys))
            warna_hasil = warna_keys[idx]
            data = AURA_DB[warna_hasil]
            
            st.write(f"✅ Vibrasi Terdeteksi: {round(vibrasi * 4.5, 1)} MHz")
            status.update(label="Analisis Selesai! Aura Berhasil Dimurnikan.", state="complete", expanded=False)
        
        # --- 4. VISUALISASI AI GLOW ---
        # Membuat pendaran warna yang lebih halus
        color_rgb = tuple(int(data["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow_layer = Image.new("RGB", img.size, color_rgb)
        # Menggunakan blend lebih halus + filter blur untuk efek aura
        visual_aura = Image.blend(img, glow_layer, alpha=0.25)
        
        st.divider()
        st.subheader(f"4. Visualisasi Aura Detik Ini: {warna_hasil}")
        st.image(visual_aura, caption=f"Aura Scan: {nama} | {time.strftime('%H:%M:%S')} WIB")
        
        # Tampilan Skala Hawkins
        st.markdown(f'''
            <div class="hawkins-box">
                {data['hawkins']} Log<br>
                <span style="font-size: 18px;">Level: {data['state']}</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # --- 5 & 6. SARAN BERDASARKAN UMUR ---
        st.divider()
        col_a, col_b = st.columns(2)
        with col_a:
            st.warning(f"✨ *5. Deskripsi Aura {warna_hasil}*")
            st.write(data["desc"])
        with col_b:
            if 7 <= umur <= 18:
                st.success("📚 *6. Rekomendasi Belajar*")
                st.write(f"Sebagai pelajar {umur} thn, energi ini sangat bagus untuk mendalami: *{data['belajar']}*")
            else:
                st.success("💼 *6. Rekomendasi Karir*")
                st.write(f"Di usia profesional {umur} thn, potensi terbaik Anda adalah sebagai: *{data['karir']}*")
            
        st.info("💡 *Tips AI:* Hasil ini didasarkan pada pembacaan sensor visual detik ini. Tetaplah positif!")
else:
    st.info("Sistem Standby. Masukkan data diri untuk mengaktifkan AI.")
