#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin
yeni_liste = [1, 2, 3, 4, 5]
tuple = (8, 9)
print ("listenizin şu an: ", yeni_liste)
yeni_liste.insert(3, tuple)
print ("yeni listeniz: ", yeni_liste)


#list = [1, 2, 3, 4, 5]
#tuple_ekle = (6, 7)
#ortasina_tuple_ekle(list, tuple_ekle)
#def ortasina_tuple_ekle(liste, tuple_ekle):
#    uzunluk = len(liste)
#    orta_index = uzunluk // 2
#    liste.insert(orta_index, tuple_ekle)