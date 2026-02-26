sonlar = list(range(1, 101))

for son in sonlar:
    if son % 2 != 0:
        print(f"Toq son: {son}")

juft_sonlar = []
toq_sonlar = []

for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)
son_2 = 100
juft_son = []
toq_son = []

for son in range(1, son_2 + 1):
    if son % 2 == 0:
        juft_son.append(son)
    else:
        toq_son.append(son)


print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)
print(f"{son_2} juft sonlar:", juft_son)
print(f"{son_2} toq sonlar:", toq_son)



son = int(input("son kiriting: "))


toq_sonlar = []
juft_sonlar = []

for son in range(1, son + 1):
    if son % 2 == 0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)

print(f"\n1 dan {son} toq sonlar:")
print(toq_sonlar)

print(f"\n1 dan {son} juft sonlar:")
print(juft_sonlar)




'''
import math

print(math.ceil(8.7))
print(math.floor(8.7))
print(math.sqrt(54))

'''

#ikki xil vaqt kiritiladi
#time1 = soat1, minut1 second1
#time2 = soat2, minut2  second2

soat1 = int(input('1-soat:'))
minut1 = int(input('1-minut:'))
second1 = int(input('1-second:'))

soat2 = int(input('2-soat:'))
minut2 = int(input('2-minut:'))
second2 = int(input('2-second:'))

#1 soat 3600 second, 1minut 60 second

second = (soat1-soat2) * 3600 + (minut2-minut1)*60 + (second2 - second1) 
print('second {}'.format(second))

