import streamlit as st
from PIL import Image, ImageOps, ImageStat
import time
import base64
from fpdf import FPDF

# --- 1. KONFIGURASI HALAMAN & STYLE ---
st.set_page_config(page_title="AuraLens Pro Max AI - Official", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    div.stButton > button:first-child { 
        width: 100%; background-color: #4B0082; color: white; 
        border-radius: 12px; font-weight: bold; border: 2px solid #FFD700;
        transition: 0.3s;
    }
    div.stButton > button:hover { border: 2px solid #FFFFFF; background-color: #6A0DAD; }
    .hawkins-box {
        font-size: 26px; font-weight: bold; text-align: center; color: #FFFFFF;
        background: linear-gradient(45deg, #4B0082, #000000);
        border-radius: 15px; padding: 20px; border: 2px solid #FFD700; margin: 15px 0px;
        box-shadow: 0px 0px 15px rgba(138, 43, 226, 0.5);
    }
    .spectrum-bar { height: 12px; width: 100%; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-radius: 10px; margin: 10px 0px; }
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border-left: 6px solid #4B0082; margin-top: 20px; }
    .lifestyle-box { background-color: #262730; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #333; }
    .copyright { text-align: center; font-size: 13px; color: #888; margin-top: 60px; border-top: 1px solid #333; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATABASE MASTER (BLUEPRINT & LIFESTYLE) ---
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Action/Anger", "vibe": "Api (Ekspansif)",
        "blueprint": "Pelopor Berani & Tak Kenal Takut. Anda lahir untuk membuka jalan baru dan memimpin perubahan fisik.",
        "hobi": "Bela diri/Gym", "hewan": "Anjing Penjaga", "tanaman": "Kaktus/Mawar", "karir": "Atlet/CEO"
    },
    "Jingga": {
        "hex": "#FF7F00", "hawkins": 200, "state": "Courage", "vibe": "Kreatif (Mengalir)",
        "blueprint": "Pencipta Ekspresif. Jiwa Anda bersinar saat mengolah ide imajinatif menjadi karya nyata.",
        "hobi": "Masak/Seni", "hewan": "Kucing Tabby", "tanaman": "Bunga Matahari", "karir": "Animator/Artis"
    },
    "Kuning": {
        "hex": "#FFFF00", "hawkins": 310, "state": "Willingness", "vibe": "Cahaya (Logika)",
        "blueprint": "Pemikir Logis & Cerdas. Anda adalah sumber solusi dan pengetahuan yang menerangi ketidakpastian.",
        "hobi": "Catur/Coding", "hewan": "Burung Beo", "tanaman": "Mint/Lemon", "karir": "IT/Ilmuwan"
    },
    "Hijau": {
        "hex": "#00FF00", "hawkins": 400, "state": "Reason", "v
