import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import base64
from fpdf import FPDF

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro Max AI", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700;
    }
    .hawkins-box {
        font-size: 24px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; margin: 15px 0px;
    }
    .spectrum-bar { height: 12px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet, grey, maroon, black); border-radius: 10px; margin: 15px 0px; }
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border-left: 6px solid #FFD700; margin-top: 20px; }
    .warning-card { background-color: #2D1B1B; padding: 15px; border-radius: 10px; border-left: 6px solid #FF4B4B; margin-top: 10px; color: #FFCDCD; }
    .motivation-card { background-color: #1B2D1B; padding: 15px; border-radius: 10px; border-left: 6px solid #4BFF4B; margin-top: 10px; color: #CDFFCD; }
    .copyright { text-align: center; font-size: 12px; color: #888; margin-top: 50px; border-top: 1px solid #333; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Life Blueprint Analysis - Version 2.0")

# --- DATABASE MASTER (DENGAN TAMBAHAN WARNA & MOTIVASI) ---
AURA_DB = {
    "Merah": {"hex": "#FF0000", "hawkins": 150, "state": "Action", "tantangan": "Cenderung impulsif dan mudah marah jika keinginan tidak terpenuhi.", "solusi": "Salurkan energimu ke olahraga atau karya kreatif. Ingat, kesabaran adalah kekuatan yang tenang."},
    "Jingga": {"hex": "#FF7F00", "hawkins": 200, "state": "Courage", "tantangan": "Sering merasa cemas berlebihan tentang penilaian orang lain.", "solusi": "Fokuslah pada proses berkarya, bukan hasil akhir. Duniamu tetap indah meski tidak semua orang melihatnya."},
    "Kuning": {"hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "tantangan": "Terlalu banyak berpikir (overthinking) hingga lupa beraksi.", "solusi": "Ilmu tanpa amal itu hampa. Mulailah satu langkah kecil hari ini, jangan tunggu sempurna."},
    "Hijau": {"hex": "#00FF00", "hawkins": 400, "state": "Reason", "tantangan": "Sering mendahulukan orang lain hingga mengabaikan diri sendiri.", "solusi": "Kamu tidak bisa menuang air dari gelas yang kosong. Cintai dirimu sendiri sebelum menyembuhkan dunia."},
    "Biru": {"hex": "#0000FF", "hawkins": 500, "state": "Love", "tantangan": "Kadang sulit mengungkapkan perasaan jujur karena takut konflik.", "solusi": "Suaramu berharga. Berbicara jujur dengan kasih sayang akan membuka pintu yang selama ini tertutup."},
    "Nila": {"hex": "#4B0082", "hawkins": 540, "state": "Joy", "tantangan": "Merasa kesepian karena merasa tidak ada yang memahami visi besarmu.", "solusi": "Temukan komunitas yang sefrekuensi. Kamu tidak perlu berjalan sendirian untuk mencapai bintang."},
    "Ungu": {"hex": "#800080", "hawkins": 600, "state": "Peace", "tantangan": "Bisa menjadi terlalu idealis dan jauh dari realita praktis.", "solusi": "Tetaplah membumi. Gunakan kebijaksanaanmu untuk membantu hal-hal nyata di sekitarmu."},
    "Abu-Abu": {"hex": "#808080", "hawkins": 250, "state": "Neutrality", "tantangan": "Kurang semangat dan merasa hidup terasa datar atau membosankan.", "solusi": "Cobalah hal baru di luar zona nyamanmu. Sedikit percikan keberanian akan mewarnai harimu."},
    "Marun": {"hex": "#800000", "hawkins": 175, "state": "Intensity", "tantangan": "Menyimpan tekanan batin yang kuat dan keras pada diri sendiri.", "solusi": "Maafkan kesalahan masa lalu. Kamu sedang berproses, dan itu sudah lebih dari cukup."},
    "Hitam": {"hex": "#1A1A1A", "hawkins": 100, "state": "Protection", "tantangan": "Menutup diri terlalu rapat karena takut disakiti kembali.", "solusi": "Perisai melindungimu, tapi juga menghalangimu melihat cahaya. Beranilah terbuka pada orang yang tepat."}
}

# --- 1. INPUT DATA ---
c1, c2 = st.columns([3, 1])
with c1:
    nama = st.text_input("1. Nama Lengkap:", placeholder="Contoh: Rocky")
with c2:
    umur = st.number_input("Umur:", min_value=7, max_value=60, value=9)

if nama:
    st.divider()
    foto = st.camera_input("2. Pindai Prana & Energi Bio-Foton")

    if foto:
        with st.status("🧬 Menganalisis Spektrum Energi...", expanded=False) as status:
            time.sleep(2)
            img = Image.open(foto)
            img = ImageOps.exif_transpose(img)
            stat = ImageStat.Stat(img)
            # Menghitung index berdasarkan kecerahan gambar
            brightness = sum(stat.mean) / 3 
            warna_keys = list(AURA_DB.keys())
            warna_hasil = warna_keys[int(brightness % len(warna_keys))]
            res = AURA_DB[warna_hasil]
            status.update(label=f"Aura {warna_hasil} Terdeteksi!", state="complete")

        # Visualisasi Aura
        c_rgb = tuple(int(res["hex"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        glow = Image.new("RGB", img.size, c_rgb)
        visual = Image.blend(img, glow, alpha=0.3)
        
        st.subheader(f"Hasil Analisis: Aura {warna_hasil}")
        st.image(visual, use_container_width=True)
        
        st.markdown(f'<div class="hawkins-box">{res["hawkins"]} Log | Status: {res["state"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="spectrum-bar"></div>', unsafe_allow_html=True)

        # Deskripsi Tantangan (Sisi Kurang Baik)
        st.markdown(f"""
        <div class="warning-card">
        <h4 style='margin:0;'>⚠️ Tantangan Saat Ini</h4>
        {res['tantangan']}
        </div>
        """, unsafe_allow_html=True)

        # Rekomendasi / Motivasi
        st.markdown(f"""
        <div class="motivation-card">
        <h4 style='margin:0;'>✨ Solusi & Motivasi</h4>
        {res['solusi']}
        </div>
        """, unsafe_allow_html=True)

        # --- DOWNLOAD PDF ---
        st.divider()
        if st.button("📥 Download Laporan Lengkap (PDF)"):
            visual.save("temp_aura.jpg")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_fill_color(14, 17, 23)
            pdf.rect(0, 0, 210, 297, 'F')
            
            pdf.set_text_color(255, 215, 0)
            pdf.set_font("Arial", 'B', 18)
            pdf.cell(0, 20, "AURA LENS PRO: OFFICIAL REPORT", ln=True, align='C')
            
            pdf.image("temp_aura.jpg", x=55, y=40, w=100)
            pdf.ln(110)
            
            pdf.set_font("Arial", 'B', 14)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, f"Nama: {nama} | Aura: {warna_hasil}", ln=True)
            
            pdf.set_font("Arial", 'B', 12)
            pdf.set_text_color(255, 100, 100)
            pdf.cell(0, 10, "SISI TANTANGAN:", ln=True)
            pdf.set_font("Arial", '', 11)
            pdf.set_text_color(255, 255, 255)
            pdf.multi_cell(0, 7, res['tantangan'])
            
            pdf.ln(5)
            pdf.set_font("Arial", 'B', 12)
            pdf.set_text_color(100, 255, 100)
            pdf.cell(0, 10, "SOLUSI MOTIVASI:", ln=True)
            pdf.set_font("Arial", '', 11)
            pdf.set_text_color(255, 255, 255)
            pdf.multi_cell(0, 7, res['solusi'])
            
            pdf.ln(10)
            pdf.set_font("Arial", 'I', 10)
            pdf.set_text_color(150, 150, 150)
            pdf.cell(0, 10, "Copyright 2026 Namikor. All Rights Reserved.", ln=True, align='C')
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="AuraReport_{nama}.pdf" style="color:white; text-decoration:none; background:#4B0082; padding:15px; border-radius:10px; display:block; text-align:center; border: 1px solid #FFD700;">KLIK DI SINI UNTUK DOWNLOAD PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

   # Pakai st.caption saja supaya lebih aman dari 'pop-up' bantuan di HP
st.caption("© 2026 Namikor. All Rights Reserved.")
