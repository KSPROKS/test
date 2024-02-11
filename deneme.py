hedef_string = "Merhaba dünya!"
hedef_karakter = "a"
def karakter_sayisi(hedef_string, hedef_karakter):
    sayac = 0
    for karakter in hedef_string:
        if karakter == hedef_karakter:
            sayac += 1
            if sayac > 0:
                return sayac
            else:
                print (f"{hedef_karakter} karakteri {hedef_string} içinde {sayac} kez geçiyor.")