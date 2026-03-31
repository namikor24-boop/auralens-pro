import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from fpdf import FPDF
import base64

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="AuraLens Pro", page_icon="🔮", layout="centered")

# --- 2. DATABASE SPEKTRUM AURA (KARIR & PENYEIMBANG) ---
AURA_DATABASE = {
    "Emas": {
        "deskripsi": "Intelektualitas tinggi dan kepemimpinan visioner.",
        "karir": "CEO, Strategist, Mentor, Tech Lead.",
        "hewan": "Kuda (Kekuatan & Marwah)",
        "benda": "Jam Tangan Logam / Emas (Disiplin)",
        "warna_bgr": (0, 215, 255)  # Gold
    },
    "Cyan (Biru-Hijau)": {
        "deskripsi": "Keseimbangan emosional dan komunikasi yang jujur.",
        "karir": "HRD, Konselor, Guru, Public Relations.",
        "hewan": "Burung (Kebebasan Visi)",
        "benda": "Mint Aromaterapi / Lapis Lazuli",
        "warna_bgr": (255, 255, 0)  # Cyan
    },
    "Merah": {
        "deskripsi": "Vitalitas tinggi, keberanian, dan energi eksekusi.",
        "karir": "Sales, Founder Startup, Atlet, Manager Lapangan.",
        "hewan": "Kucing (Meredam Stres/Tenang)",
        "benda": "Tanaman Air / Kristal Amethyst",
        "warna_bgr": (0, 0, 255)  # Red
    },
    "Ungu (Violet)": {
        "deskripsi": "Intuisi tajam dan kreativitas out-of-the-box.",
        "karir": "Desainer, Art Director, Inovator, Penulis.",
        "hewan": "Gajah (Grounding/Bijak)",
        "benda": "Batu Hitam / Black Tourmaline",
        "warna_bgr": (255, 0, 255)  # Violet
    }
}

# --- 3. UI UTAMA ---
st.title("🔮 AuraLens Pro: AI Scanner")
st.markdown("### Visualisasikan Energimu & Temukan Navigasi Karirmu")

# --- 4. SIDEBAR INPUT ---
with st.sidebar:
    st.header("Profil Scan")
    nama = st.text_input("Nama Lengkap", placeholder="Contoh: Mbak Ayi")
    opsi_aura = st.selectbox("Pilih Vibrasi Dominan:", list(AURA_DATABASE.keys()))
    run_cam = st.checkbox("Aktifkan AI Camera Scan")
    st.divider()
    st.info("Letakkan tanganmu di atas meja seolah menyentuh sensor saat scan berlangsung.")

# --- 5. LOGIKA KAMERA AI ---
if run_cam:
    if not nama:
        st.warning("⚠️ Mohon masukkan nama Anda terlebih dahulu.")
    else:
        # Inisialisasi MediaPipe Selfie Segmentation
        mp_selfie = mp.solutions.selfie_segmentation
        with mp_selfie.SelfieSegmentation(model_selection=0) as segment:
            cap = cv2.VideoCapture(0)
            FRAME_WINDOW = st.image([])
            
            st.success(f"🔮 Sedang mensinkronisasi aura {nama}... (Hapus centang untuk berhenti)")
            
            bgr_color = AURA_DATABASE[opsi_aura]["warna_bgr"]

            while run_cam:
                ret, frame = cap.read()
                if not ret: break
                
                frame = cv2.flip(frame, 1) # Mirror effect
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Proses Segmentasi Tubuh
                results = segment.process(rgb_frame)
                mask = results.segmentation_mask > 0.1
                
                # Membuat Efek Glow Aura
                aura_canvas = np.zeros(frame.shape, dtype=np.uint8)
                aura_canvas[:] = bgr_color
                
                # Masking area tubuh
                aura_glow = cv2.bitwise_and(aura_canvas, aura_canvas, mask=mask.astype(np.uint8))
                aura_glow = cv2.GaussianBlur(aura_glow, (91, 91), 0) # Efek pendaran halus
                
                # Gabungkan dengan frame asli
                combined = cv2.addWeighted(frame, 0.7, aura_glow, 0.8, 0)
                
                # Tambahkan Teks Real-time
                cv2.putText(combined, f"Scanning: {nama}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                FRAME_WINDOW.image(combined, channels="BGR")
            cap.release()

# --- 6. HASIL ANALISIS & PENYEIMBANG ---
if nama and not run_cam:
    data = AURA_DATABASE[opsi_aura]
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💼 Career Path")
        st.info(f"**Aura:** {opsi_aura}")
        st.write(f"**Deskripsi:** {data['deskripsi']}")
        st.success(f"**Profesi Cocok:** {data['karir']}")

    with col2:
        st.subheader("⚖️ Aura Balancer")
        st.warning(f"**Totem Hewan:** {data['hewan']}")
        st.warning(f"**Benda Penyeimbang:** {data['benda']}")

    # --- 7. GENERATE PDF REPORT (PREMIUM) ---
    if st.button("Generate Premium Report (PDF)"):
        pdf = FPDF()
        pdf.add_page()
        
        # Header
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(200, 20, "AuraLens Pro: Career Navigation", ln=True, align='C')
        
        # Data
        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        pdf.cell(200, 10, f"Nama: {nama}", ln=True)
        pdf.cell(200, 10, f"Aura Terdeteksi: {opsi_aura}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Analisis: {data['deskripsi']}")
        pdf.ln(5)
        pdf.cell(200, 10, f"Rekomendasi Karir: {data['karir']}", ln=True)
        pdf.cell(200, 10, f"Penyeimbang Mingguan: {data['hewan']} & {data['benda']}", ln=True)
        
        # Footer
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(200, 10, "Laporan ini dihasilkan oleh AuraLens Pro Digital Lab.", align='C')

        # Download Link
        pdf_data = pdf.output(dest='S').encode('latin-1')
        b64 = base64.b64encode(pdf_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="AuraLens_Report_{nama}.pdf" style="padding:10px; background-color:#FF4B4B; color:white; border-radius:10px; text-decoration:none;">Download PDF Report Kamu Di Sini!</a>'
        st.markdown(href, unsafe_allow_html=True)
