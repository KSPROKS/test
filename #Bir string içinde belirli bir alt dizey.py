#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin
str = input("lütfen bir string girin: ")
aranan_substring = input("lütfen aranacak alt dizeyi girin: ")
eklenecek_substring = input("lütfen yerine eklenecek alt dizeyi girin: ")
sonuc_str = str.replace(aranan_substring, eklenecek_substring)
print("sonuç:", sonuc_str)