#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin
kelime = input("lütfen bir kelime girin: ")
ters_kelime = kelime[::-1]
if kelime == ters_kelime:
    print("girilen kelime bir palindrome kelime dir")
else:
    print("girilen kelime bir palindrome kelime değildir (palindrome ye örnek olarak: 'neden' kelimesi)")