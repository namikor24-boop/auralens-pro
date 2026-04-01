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
    .blueprint-card { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border-left: 6px solid #FFD700; margin-top: 20px; }
    .career-card { background-color: #16213E; padding: 15px; border-radius: 10px; border-left: 6px solid #00D1FF; margin-top: 10px; }
    .learning-card { background-color: #1B262C; padding: 15px; border-radius: 10px; border-left: 6px solid #A2FF00; margin-top: 10px; }
    .warning-card { background-color: #2D1B1B; padding: 15px; border-radius: 10px; border-left: 6px solid #FF4B4B; margin-top: 10px; color: #FFCDCD; }
    .motivation-card { background-color: #1B2D1B; padding: 15px; border-radius: 10px; border-left: 6px solid #4BFF4B; margin-top: 10px; color: #CDFFCD; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 AuraLens Pro Max AI")
st.caption("Advanced Biometric Life Blueprint Analysis - Version 4.0")

# --- DATABASE MASTER ---
AURA_DB = {
    "Merah": {
        "hex": "#FF0000", "hawkins": 150, "state": "Action",
        "tantangan": "Cenderung impulsif dan mudah marah.",
        "solusi": "Salurkan energimu ke olahraga atau karya kreatif.",
        "karir": "CEO, Atlet Profesional, Komandan Militer, Entrepreneur.",
        "belajar": "Public Speaking, Manajemen
