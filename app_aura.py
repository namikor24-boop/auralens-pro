import tkinter as tk
import random

# Data Warna, Sisi Tantangan, dan Motivasi
aura_data = [
    {
        "warna": "#4B0082", "nama": "Ungu Tua", 
        "tantangan": "Terasa berat dan penuh misteri yang menekan.",
        "motivasi": "Misteri bukan untuk ditakuti. Di balik ketidaktahuan, ada potensi raksasa yang menunggumu!"
    },
    {
        "warna": "#708090", "nama": "Abu-Abu Baja", 
        "tantangan": "Terkesan dingin dan tidak punya perasaan.",
        "motivasi": "Jadilah teguh seperti baja. Fokuslah pada tujuanmu di tengah badai emosi."
    },
    {
        "warna": "#800000", "nama": "Merah Marun", 
        "tantangan": "Menyimpan amarah atau ketegangan yang serius.",
        "motivasi": "Ubah energi lelahmu menjadi bahan bakar. Keberanian sejati adalah tetap melangkah!"
    },
    {
        "warna": "#CC5500", "nama": "Oranye Senja", 
        "tantangan": "Terlihat berisik dan terlalu memaksakan perhatian.",
        "motivasi": "Kreativitasmu adalah cahayamu. Biarkan ia bersinar tanpa perlu meminta izin siapa pun."
    }
]

class AuraLensApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Aura Lens - Mood & Motivation")
        self.root.geometry("500x400")
        
        # Label Judul
        self.label_judul = tk.Label(root, text="Lensa Aura Mbak Ayi", font=("Arial", 18, "bold"))
        self.label_judul.pack(pady=10)

        # Frame untuk tampilan warna
        self.canvas = tk.Canvas(root, width=200, height=100, bg="white", highlightthickness=2)
        self.canvas.pack(pady=10)

        # Label Deskripsi (Sisi Tantangan)
        self.label_tantangan = tk.Label(root, text="Klik tombol untuk cek Aura", wraplength=400, fg="red", font=("Arial", 10, "italic"))
        self.label_tantangan.pack(pady=5)

        # Label Motivasi
        self.label_motivasi = tk.Label(root, text="", wraplength=400, font=("Arial", 12, "bold"), fg="darkblue")
        self.label_motivasi.pack(pady=20)

        # Tombol Update
        self.btn = tk.Button(root, text="Update Aura", command=self.update_aura, bg="#333", fg="white", padx=20)
        self.btn.pack(pady=10)

    def update_aura(self):
        # Pilih data acak
        pilihan = random.choice(aura_data)
        
        # Update tampilan
        self.canvas.configure(bg=pilihan["warna"])
        self.label_tantangan.configure(text=f"Tantangan {pilihan['nama']}: {pilihan['tantangan']}")
        self.label_motivasi.configure(text=pilihan["motivasi"])

# Menjalankan Aplikasi
if _name_ == "_main_":
    root = tk.Tk()
    app = AuraLensApp(root)
    root.mainloop()
