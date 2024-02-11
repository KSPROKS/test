#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın
set ={1,2,3,4,5}
print("set (ekleme öncesi):", set)
yeni_sayi = 6
set.add(yeni_sayi)
print("oluşan set (ekleme sonrasi):", set)
kaldirilacak_sayi = 6
set.remove(kaldirilacak_sayi)
print("oluşturulan set (çikarma sonrasi):", set)