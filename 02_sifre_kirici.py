"""
02_sifre_kirici.py
------------------
Odevin IKINCI adimi: sifreli ZIP'lerin sifresini BULMAYA calisir.

Iki yontem gosteriyoruz:
  1) WORDLIST (sozluk saldirisi): onceden hazirlanmis kelime listesini sirayla dener.
  2) BRUTE-FORCE (kaba kuvvet): tum harf/rakam kombinasyonlarini uretip dener.

Mantik ayni: "dogru sifre, ZIP'i hatasiz acan sifredir".
Yanlis sifrede kutuphane hata firlatir -> onu yakalayip sonraki sifreyi deneriz.

!! Egitim amaclidir. Sadece KENDI olusturdugun dosyalar uzerinde calistir. !!
"""

import itertools
import string
import time

import pyzipper


def sifreyi_dene(zip_adi: str, sifre: str) -> bool:
    """Verilen sifre dogruysa True, yanlissa False doner."""
    try:
        with pyzipper.AESZipFile(zip_adi) as zf:
            zf.setpassword(sifre.encode("utf-8"))
            # Arsivdeki ilk dosyayi okumaya calisiyoruz; sifre yanlissa hata firlar.
            zf.read(zf.namelist()[0])
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# YONTEM 1: Kelime listesi (wordlist) saldirisi
# ---------------------------------------------------------------------------
def wordlist_saldirisi(zip_adi: str, kelimeler: list):
    print(f"\n=== YONTEM 1: Wordlist saldirisi  ->  {zip_adi} ===")
    basla = time.time()
    for i, sifre in enumerate(kelimeler, start=1):
        print(f"  Deneniyor ({i}/{len(kelimeler)}): {sifre}")
        if sifreyi_dene(zip_adi, sifre):
            sure = time.time() - basla
            print(f"[+] BULUNDU! Sifre = '{sifre}'  ({i} denemede, {sure:.2f} sn)")
            return sifre
    print("[-] Wordlist'te sifre bulunamadi.")
    return None


# ---------------------------------------------------------------------------
# YONTEM 2: Kaba kuvvet (brute-force) saldirisi
# ---------------------------------------------------------------------------
def brute_force_saldirisi(zip_adi: str, karakterler: str, max_uzunluk: int):
    print(f"\n=== YONTEM 2: Brute-force saldirisi  ->  {zip_adi} ===")
    print(f"  Karakter seti: {karakterler}")
    print(f"  En fazla uzunluk: {max_uzunluk}")
    basla = time.time()
    deneme = 0
    for uzunluk in range(1, max_uzunluk + 1):
        for kombinasyon in itertools.product(karakterler, repeat=uzunluk):
            sifre = "".join(kombinasyon)
            deneme += 1
            if sifreyi_dene(zip_adi, sifre):
                sure = time.time() - basla
                print(f"[+] BULUNDU! Sifre = '{sifre}'  ({deneme} denemede, {sure:.2f} sn)")
                return sifre
    print(f"[-] {deneme} deneme yapildi, sifre bulunamadi.")
    return None


if __name__ == "__main__":
    # --- Yontem 1: gizli.zip (sifre: kedi123) ---
    # Gercek dunyada bu listeler 'rockyou.txt' gibi milyonlarca satir olur.
    ornek_wordlist = [
        "123456", "password", "qwerty", "admin",
        "deneme", "kopek123", "kedi123", "sifre",
    ]
    wordlist_saldirisi("gizli.zip", ornek_wordlist)

    # --- Yontem 2: kolay.zip (sifre: a7) ---
    # Kucuk harf + rakam, en fazla 2 karakter -> kisa sifreyi hizlica bulur.
    brute_force_saldirisi(
        "kolay.zip",
        karakterler=string.ascii_lowercase + string.digits,
        max_uzunluk=2,
    )

    print("\nDERSIN OZETI: Sifre kisa ve tahmin edilebilirse saniyeler icinde kirilir.")
    print("Uzun + rastgele sifre, brute-force'u pratikte imkansiz kilar.")
