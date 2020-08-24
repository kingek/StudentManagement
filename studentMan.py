
say=10 #Telebe sayinin daxil edilmesi
# say = input("sayi daxil et :")
say=int(say)



userList=[]


class Istifadeci:
    def __init__(self,_kodu,_ad,_soyad,_email,_phone):
        self.kodu=_kodu
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.phone=_phone

        userList.append(self)
    def melumatlariGoster(self):
        print("Telebe kodu: " + self.kodu + " / " + "Telebenin adi: " + self.ad + " / " + "Soyadi: " + self.soyad + " / " + "Email: " + self.email + " / "+ "Elaqe nomresi: " + self.phone)
    
i=1
while i<=say:
    kodu = int(input("Telebe kodu (yalniz reqem daxil edin) :"))
    ad = input("Ad :")
    soyad = input("Soyad :")
    email = input("Email :")
    phone = input("Elaqe nomresi :")
    yeniIstifadeci = Istifadeci(kodu, ad, soyad, email, phone)
    i+=1

print("--------------")


emr=input("Melumatlara baxmaq ucun 1 yazin : ")


if(emr=="1"):
    for istifadeci in userList:
        istifadeci.melumatlariGoster()

else:
    print("Emr duzgun deyil")


emr2=input("Telebe adina gore melumatlari tapmaq ucun 2 yaz : ")

if(emr2=="2"):
    ad = input("Ad :")
    for ad in userList:
        istifadeci.melumatlariGoster()
        break
    

else:
    print("Emr duzgun deyil")


    
     
emr3=input("Telebe koduna gore telebeni silmek ucun 3 yaz : ")

if(emr3=="3"):
    kodu = input("Telebe kodu :")
    for kodu in userList:
        userList.remove(ad)
        break

   
    

else:
    print("Emr duzgun deyil")


    

emr4=input("Telebelerin siyahisina baxmaq ucun 4 secin : ")

if(emr4=="4"):
    for istifadeci in userList:
        istifadeci.melumatlariGoster()

else:
    print("Emr duzgun deyil")



# emr5=input("Telebe koduna gore telebenin melumatlarini deyismek ucun 5 yaz : ")



# if(emr5=="5"):

    


    
#     kodu = input("Telebe kodu :")
#     for kodu in userList:
        
#         userList.update(ad)
#         break

#     emr6=input("Telebelerin siyahisina baxmaq ucun 6 secin : ")

# if(emr6=="6"):
#     for istifadeci in userList:
#         istifadeci.melumatlariGoster()

# else:
#     print("Emr duzgun deyil")