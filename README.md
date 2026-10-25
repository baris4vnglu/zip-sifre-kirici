# ZIP Şifre Kırıcı — Okul Ödevi

Bu ödev, bir **şifre korumalı ZIP dosyasının** nasıl oluşturulduğunu ve
şifresinin iki klasik yöntemle nasıl bulunduğunu (kırıldığını) gösterir.

> ⚠️ **Sadece eğitim amaçlıdır.** Scriptleri yalnızca **kendi oluşturduğun**
> dosyalar üzerinde çalıştır. Başkasına ait dosya/hesap şifrelerini kırmak yasa dışıdır.

## Dosyalar

| Dosya | Görevi |
|-------|--------|
| `01_zip_olustur.py` | Şifreli iki demo ZIP üretir (`gizli.zip`, `kolay.zip`) |
| `02_sifre_kirici.py` | Bu ZIP'lerin şifresini wordlist + brute-force ile bulur |

## Gereksinim

```bash
python -m pip install pyzipper
```

> Python'un standart `zipfile` kütüphanesi şifreli ZIP **oluşturamaz** (sadece
> okuyabilir), bu yüzden AES şifreleme destekleyen `pyzipper` kullanıyoruz.

## Nasıl çalıştırılır

```bash
python 01_zip_olustur.py
python 02_sifre_kirici.py
```

## İki yöntem

1. **Wordlist (sözlük saldırısı):** Önceden hazırlanmış kelime listesindeki
   şifreleri sırayla dener. Gerçek dünyada `rockyou.txt` gibi milyonlarca
   satırlık listeler kullanılır. `gizli.zip` (şifre: `kedi123`) bu yöntemle bulunur.
2. **Brute-force (kaba kuvvet):** Belirlenen karakter setiyle tüm olası
   kombinasyonları üretip dener. `kolay.zip` (şifre: `a7`) bu yöntemle bulunur.

## İşin püf noktası (sunum/rapor için)

Her iki yöntemin de mantığı aynı: **doğru şifre, ZIP'i hatasız açan şifredir.**
Yanlış şifrede kütüphane hata fırlatır; biz bu hatayı yakalayıp bir sonrakini deneriz.

**Dersin özeti:** Şifre kısa ve tahmin edilebilirse saniyeler içinde kırılır.
Karakter seti ve uzunluk büyüdükçe deneme sayısı **katlanarak** artar — bu yüzden
uzun ve rastgele şifreler brute-force'u pratikte imkânsız kılar.

| Şifre uzunluğu (küçük harf + rakam, 36 karakter) | Olası kombinasyon |
|---|---|
| 2 | 1.296 |
| 4 | ~1,6 milyon |
| 8 | ~2,8 **trilyon** |
