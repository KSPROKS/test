#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin
yeni_liste = [1, 2, 3, 4, 5, 6]
print("listeniz şu an:",yeni_liste)
yeni_sayi = int(input("lütfen listeye eklemek istediğiniz sayiyi girin: "))
yeni_liste.insert(3, yeni_sayi)
print("yeni listeniz:", yeni_liste)



#yeni_liste = [1, 2, 3, 4, 5]
#yeni_sayi = int(input("lütfen listeye eklemek istediğiniz sayiyi girin: "))
#def ortaya_sayi_ekle(yeni_liste, yeni_sayi):
#    orta_indeks = len(yeni_liste) // 2
#    yeni_liste.insert(orta_indeks, yeni_sayi)
#    print("yeni listeniz:", yeni_liste)