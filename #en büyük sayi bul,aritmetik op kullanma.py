#Bir liste oluşturun ve listenin içindeki en büyükk sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın
yeni_list = [3, 7, 1, 9, 4, 6, 8, 2, 5]
def en_buyuk_sayi(liste):
    max_sayi = None
    for sayi in liste:
        if max_sayi is None or sayi > max_sayi:
            max_sayi = sayi
    return max_sayi
max_sayi = en_buyuk_sayi(yeni_list)
print("liste:", yeni_list)
print("en büyük sayi:", max_sayi)