def guvenli_bolme(a, b):
    try:
        sonuc = a / b
        print(f"{a} / {b} = {sonuc}")
    except ZeroDivisionError:
        print("HATA: Sıfıra bölmeye çalıştınız!")
    except TypeError:
        print("HATA: Lütfen sayı girin!")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

guvenli_bolme(10, 2)    # Çalışır
guvenli_bolme(10, 0)    # ZeroDivisionError yakalar
guvenli_bolme(10, "a")  # TypeError yakalar

"""
ALIŞTIRMA: YAŞ SORGULAMA PROGRAMI
Kullanıcıdan yaşını isteyen, hatalı girişleri yöneten program
"""

def yas_sorgula():
    while True:
        try:
            yas = int(input("Yaşınızı girin (0-120): "))
            
            if yas < 0 or yas > 120:
                print("HATA: Yaş 0 ile 120 arasında olmalı!")
                continue
                
            print(f"Yaşınız: {yas}")
            break
            
        except ValueError:
            print("HATA: Lütfen geçerli bir sayı girin!")
        except KeyboardInterrupt:
            print("\nProgram kapatıldı.")
            break

yas_sorgula()