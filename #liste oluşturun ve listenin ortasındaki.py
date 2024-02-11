#liste oluşturun ve listenin ortasındaki elemanı bulun
liste_str = input("lütfen bir liste girin (ör: 1, 2, 3): ")
liste = [int(eleman) for eleman in liste_str.split(",")]
def orta_elemani_bul(liste):
    uzunluk = len(liste)
    orta_indis = uzunluk // 2
    print ("Listenin ortasindaki eleman:", liste[orta_indis])