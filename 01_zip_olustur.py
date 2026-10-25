"""
01_zip_olustur.py
------------------
Odevin BIRINCI adimi: SIFRE KORUMALI iki ZIP dosyasi uretir.
Bu dosyalari daha sonra 02_sifre_kirici.py ile kiracagiz.

  * gizli.zip -> uzun sifre ("kedi123") -> WORDLIST yontemiyle bulunur.
  * kolay.zip -> kisa sifre ("a7")      -> BRUTE-FORCE yontemiyle bulunur.

Not: Python'un standart 'zipfile' kutuphanesi sifreli ZIP OLUSTURAMAZ
(sadece okuyabilir). Bu yuzden AES sifreleme destekleyen 'pyzipper' kullaniyoruz.
"""

import pyzipper


def sifreli_zip_olustur(zip_adi: str, sifre: str, dosya_adi: str, icerik: str):
    # AES-256 ile sifreli bir ZIP aciyoruz
    with pyzipper.AESZipFile(
        zip_adi,
        "w",
        compression=pyzipper.ZIP_DEFLATED,
        encryption=pyzipper.WZ_AES,
    ) as zf:
        zf.setpassword(sifre.encode("utf-8"))        # sifreyi byte olarak ver
        zf.writestr(dosya_adi, icerik)               # dosyayi arsive yaz
    print(f"[+] '{zip_adi}' olusturuldu  (icindeki dosya: {dosya_adi}, sifre: {sifre})")


if __name__ == "__main__":
    # Wordlist demosu icin: uzun, "sozlukte olabilecek" bir sifre
    sifreli_zip_olustur(
        "gizli.zip",
        sifre="kedi123",
        dosya_adi="mesaj.txt",
        icerik="Tebrikler! Wordlist ile sifreyi kirdin. :)",
    )

    # Brute-force demosu icin: cok kisa sifre (deneme-yanilma makul surede bulsun)
    sifreli_zip_olustur(
        "kolay.zip",
        sifre="a7",
        dosya_adi="mesaj.txt",
        icerik="Tebrikler! Brute-force ile sifreyi kirdin. :)",
    )

    print("\nHazir. Simdi: python 02_sifre_kirici.py")
