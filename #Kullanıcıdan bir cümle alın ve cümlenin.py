#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın
cumle = input("lütfn bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)
print("Cümlenin içindeki kelimeler alfabetik siraya göre:")
for kelime in sirali_kelimeler:
    print(kelime)