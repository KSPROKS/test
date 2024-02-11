#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin
dict = {"anahtar1": "değer1", "anahtar2": "değer2", "anahtar3": "değer3"}
print("oluşturulan dictionary (ekleme öncesi):", dict)
yeni_anahtar = "anahtar4"
yeni_deger = "değer4"
dict[yeni_anahtar] = yeni_deger
print("oluşturulan Dictionary (ekleme sonrasi):", dict)
silinecek_anahtar = "anahtar2"
del dict[silinecek_anahtar]
print("oluşturulan dictionary (silme sonrasi):", dict)