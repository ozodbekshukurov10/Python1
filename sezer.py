
alifbo = [
    'a','b','v','g‘','d','e','yo','j','z','i','k','l','m','n','o','p','r',
    's','t','u','f','x','h','sh','ch','ʼ','q'
]

siljitish = 3

print('1 - ozbek')
print('2 - sezer')

a = input('Qaysi biri: ')
matn = input("Matn: ")

sezer = ""
ozbek = ""

if a == '1':  
    for harf in matn:
        if harf in alifbo:
            idx = alifbo.index(harf)
            yangi = alifbo[(idx - siljitish) % len(alifbo)]
            ozbek += yangi
        else:
            ozbek += harf
    print("Ozbek:", ozbek)

elif a == '2': 
    for harf in matn:
        if harf in alifbo:
            idx = alifbo.index(harf)
            yangi = alifbo[(idx + siljitish) % len(alifbo)]
            sezer += yangi
        else:
            sezer += harf
    print("Sezer:", sezer)

else:
    print("notog‘ri")
