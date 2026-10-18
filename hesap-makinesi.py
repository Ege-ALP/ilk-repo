sayi1=float(input("Lütfen islem yapilacak sayiyi giriniz : "))
islem=input("Yapmak istediğiniz islemi seciniz : +,-,*,/")
sayi2=float(input("Lütfen ikinci sayiyi giriniz : "))

if islem == "+":
    sonuc = sayi1+sayi2
    print("Sonucunuz : ",sonuc)

elif islem == "-":
    sonuc = sayi1-sayi2
    print("Sonucunuz : ",sonuc)

elif islem == "*":
    sonuc= sayi1*sayi2
    print("Sonucunuz : ",sonuc)

elif islem == "/":
    if sayi2 != 0:
       sonuc = sayi1/sayi2
       print("Sonucunuz : ",sonuc)
    else:
       print("Sifira bölünmez.") 

else:
    print("Gecersiz islem.")       
