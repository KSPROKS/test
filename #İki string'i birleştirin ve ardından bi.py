#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bul
str1=str("Merhabalar nasilsiniz ")
str2=str("Ben iyiyim")
bilesik = str1 + str2
substring=input("lütfen bulunacak substring i girniz: ")
index = (bilesik,substring).find_substring
if index != -1:
    print(f"'{substring}' substring i birlestirilmis string icinde {index} indekste bulunuyor")
    def find_substring(main_string, substring):
        index = main_string.find(substring)
        return index
    print(bilesik[substring:])
else:
    print(f"'{substring}' substring i birlestirilmis string icinde bulunamadi")