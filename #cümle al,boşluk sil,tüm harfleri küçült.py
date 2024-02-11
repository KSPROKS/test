#cümle al,boşluk sil,tüm harfleri küçült 
cumle = input("lütfen bir cümle giriniz: ")
yeni_cumle = cumle.replace(" ", "")
kucukcumle = yeni_cumle.strip().lower()
print(kucukcumle)