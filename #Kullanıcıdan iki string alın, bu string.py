#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevir
str1 = input("lütfen birinci stringi girin: ")
str2 = input("lütfen ikinci stringi girin: ")
birlesik= str1 + str2
kucuk_harf = birlesik.lower()
print("birleştirilmis ve küçük harfe çevrilmis string:", kucuk_harf)