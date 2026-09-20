import tkinter as tk
import random

# ============================================================
# --- OYUN DEĞİŞKENLERİ ---
# ============================================================
with open("words.txt", "r", encoding="utf-8") as dosya:
    kelimeler = dosya.readlines()
kelimeler = [satir.strip().lower() for satir in kelimeler]

secilen_kelime = random.choice(kelimeler)
kalan_hak = 6
tahmin_edilenler = []

gizli_kelime = []
for harf in secilen_kelime:
    if harf == " ":
        gizli_kelime.append(" ")
    else:
        gizli_kelime.append("_")


# ============================================================
# --- PENCERE ---
# ============================================================
pencere = tk.Tk()
pencere.title("Adam Asmaca")
pencere.geometry("600x800")
pencere.config(bg="#f0f0f0")

# --- Başlık ---
baslik = tk.Label(pencere, text="🎯 Adam Asmaca",
                   font=("Segoe UI", 22, "bold"),
                   bg="#f0f0f0", fg="#333")
baslik.pack(pady=10)

# --- Canvas (adam çizimi) ---
canvas = tk.Canvas(pencere, width=250, height=250, bg="white",
                    highlightthickness=2, highlightbackground="#ccc")
canvas.pack(pady=10)

# --- Gizli kelime ---
kelime_label = tk.Label(pencere, text=" ".join(gizli_kelime),
                         font=("Courier", 24, "bold"),
                         bg="#f0f0f0", fg="#333")
kelime_label.pack(pady=15)

# --- Kalan hak ---
hak_label = tk.Label(pencere, text=f"Kalan Hak: {kalan_hak}",
                      font=("Segoe UI", 14),
                      bg="#f0f0f0", fg="#555")
hak_label.pack(pady=5)

# --- Tahmin edilenler ---
tahmin_label = tk.Label(pencere, text="Tahminler: -",
                         font=("Segoe UI", 11),
                         bg="#f0f0f0", fg="#777")
tahmin_label.pack(pady=5)

# --- Butonların çerçevesi ---
buton_cercevesi = tk.Frame(pencere, bg="#f0f0f0")
buton_cercevesi.pack(pady=15)

# --- Tekrar oyna butonu (başlangıçta gizli) ---
tekrar_buton = tk.Button(pencere, text="🔄 Tekrar Oyna",
                          font=("Segoe UI", 14, "bold"),
                          bg="#4CAF50", fg="white",
                          activebackground="#45a049",
                          padx=20, pady=8, border=0,
                          command=lambda: oyunu_sifirla())

# --- İpucu yazısı ---
ipucu_label = tk.Label(pencere,
                        text="💡 İpucu: Klavyeden de harf girebilirsin (Enter = tekrar oyna)",
                        font=("Segoe UI", 9, "italic"),
                        bg="#f0f0f0", fg="#999")
ipucu_label.pack(side="bottom", pady=5)


# ============================================================
# --- FONKSİYONLAR ---
# ============================================================

def adam_ciz(kalan_hak):
    yanlis_sayisi = 6 - kalan_hak
    canvas.delete("all")

    # İskele
    if yanlis_sayisi >= 1:
        canvas.create_line(50, 220, 50, 50, width=4, fill="#8B4513")   # direk
        canvas.create_line(50, 50, 150, 50, width=4, fill="#8B4513")   # üst
        canvas.create_line(150, 50, 150, 80, width=2, fill="#666")     # ip

    # Kafa
    if yanlis_sayisi >= 2:
        canvas.create_oval(130, 80, 170, 120, width=3, outline="#333")

    # Gövde
    if yanlis_sayisi >= 3:
        canvas.create_line(150, 120, 150, 180, width=3, fill="#333")

    # Sol kol
    if yanlis_sayisi >= 4:
        canvas.create_line(150, 140, 120, 160, width=3, fill="#333")

    # Sağ kol
    if yanlis_sayisi >= 5:
        canvas.create_line(150, 140, 180, 160, width=3, fill="#333")

    # Bacaklar
    if yanlis_sayisi >= 6:
        canvas.create_line(150, 180, 120, 220, width=3, fill="#333")
        canvas.create_line(150, 180, 180, 220, width=3, fill="#333")


def tahmin_et(harf, buton):
    global kalan_hak, gizli_kelime, tahmin_edilenler

    if harf in tahmin_edilenler:
        return

    tahmin_edilenler.append(harf)

    # Butonu devre dışı bırak + rengini ayarla
    if harf in secilen_kelime:
        buton.config(state="disabled", bg="#4CAF50", disabledforeground="white")
        for i in range(len(secilen_kelime)):
            if secilen_kelime[i] == harf:
                gizli_kelime[i] = harf
    else:
        buton.config(state="disabled", bg="#e74c3c", disabledforeground="white")
        kalan_hak -= 1

    # Ekranı güncelle
    kelime_label.config(text=" ".join(gizli_kelime))
    hak_label.config(text=f"Kalan Hak: {kalan_hak}")
    tahmin_label.config(text=f"Tahminler: {', '.join(tahmin_edilenler)}")

    # Adam çizimini güncelle
    adam_ciz(kalan_hak)

    # Kazandı mı?
    if "_" not in gizli_kelime:
        kelime_label.config(text=f"🎉 KAZANDIN! {secilen_kelime.upper()}", fg="#27ae60")
        butonlari_kapat()
        tekrar_buton.pack(pady=10)

    # Kaybetti mi?
    elif kalan_hak == 0:
        kelime_label.config(text=f"💀 KAYBETTİN! {secilen_kelime.upper()}", fg="#e74c3c")
        butonlari_kapat()
        tekrar_buton.pack(pady=10)


def butonlari_kapat():
    for buton in buton_listesi:
        buton.config(state="disabled")


def oyunu_sifirla():
    global secilen_kelime, gizli_kelime, kalan_hak, tahmin_edilenler

    secilen_kelime = random.choice(kelimeler)
    kalan_hak = 6
    tahmin_edilenler = []

    gizli_kelime = []
    for harf in secilen_kelime:
        if harf == " ":
            gizli_kelime.append(" ")
        else:
            gizli_kelime.append("_")

    kelime_label.config(text=" ".join(gizli_kelime), fg="#333")
    hak_label.config(text=f"Kalan Hak: {kalan_hak}")
    tahmin_label.config(text="Tahminler: -")
    canvas.delete("all")

    for buton in buton_listesi:
        buton.config(state="normal", bg="#ffffff")

    tekrar_buton.pack_forget()


def tus_basildi(event):
    # Oyun bittiyse ve Enter'a basıldıysa → tekrar oyna
    if event.keysym == "Return" and tekrar_buton.winfo_ismapped():
        oyunu_sifirla()
        return

    harf = event.char.lower()

    # Geçerli bir harf mi?
    if harf not in buton_sozlugu:
        return

    buton = buton_sozlugu[harf]

    # Buton zaten devre dışıysa (tahmin edilmişse) hiçbir şey yapma
    if str(buton["state"]) == "disabled":
        return

    tahmin_et(harf, buton)


# ============================================================
# --- BUTONLARI OLUŞTUR ---
# ============================================================
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
buton_listesi = []
buton_sozlugu = {}

for i, harf in enumerate(harfler):
    buton = tk.Button(
        buton_cercevesi,
        text=harf,
        width=3,
        height=1,
        font=("Segoe UI", 11),
        bg="#ffffff",
        activebackground="#ddd",
        border=1
    )
    buton.config(command=lambda h=harf, b=buton: tahmin_et(h, b))
    satir = i // 7
    sutun = i % 7
    buton.grid(row=satir, column=sutun, padx=3, pady=3)
    buton_listesi.append(buton)
    buton_sozlugu[harf] = buton


# ============================================================
# --- KLAVYE DİNLEME + BAŞLAT ---
# ============================================================
pencere.bind("<Key>", tus_basildi)
pencere.focus_force()

pencere.mainloop()