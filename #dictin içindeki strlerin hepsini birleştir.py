#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin
dict = {
    "anahtar1": "Merhaba, ",
    "anahtar2": "Dünya",
    "anahtar3": "!",
    "anahtar4": ", Python",}
def birlesik_string(dic):
    birlesik = "".join(value for value in dic.values() if isinstance(value, str))
    return birlesik
birlesik_string_deger = birlesik_string(dict)
print("Sözlük:", dict)
print("Birleştirilmiş String:", birlesik_string_deger)