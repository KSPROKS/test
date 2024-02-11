#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun
dict = {
    "anahtar1": "merhaba",
    "anahtar2": "dünya",
    "anahtar3": "python",
    "anahtar4": "geliştirici"}
def karakter_sayisi_toplami(dic):
    toplam = 0
    for value in dic.values():
        if isinstance(value, str):
            toplam += len(value)
    return toplam
toplam_karakter_sayisi = karakter_sayisi_toplami(dict)
print("sözlük:", dict)
print("dtring değerlerin toplam karakter sayisi:", toplam_karakter_sayisi)