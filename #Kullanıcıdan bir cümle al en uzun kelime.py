#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun
cumle = input("lütfen bir cümle girin: ")
kelimeler = cumle.split()
en_uzun_kelime = max(kelimeler, key=len)
print(cumle,", bu cümledeki en uzun kelime: ", en_uzun_kelime)