mevalar = ["olma", "banan", "uzum", 'nok', 'anjir', 'shaftoli']

for i, meva in enumerate(mevalar):
    print(i, meva)


print(round(3.14159, 2)) #sonni yaxslitlaydi 

import webbrowser


a = input("sonni kriting: ")

if a == '1':
    webbrowser.open("https://www.google.com")
elif a == '2':
    webbrowser.open("https://www.youtube.com")
elif a == '3':
    webbrowser.open("https://www.wikipedia.org")
else:
    print("bunday son yo'q")


import math


print()
print()
print(math.sqrt(20))
print('bu ilzini chuiqaruiadi ')   # 4.0   ildiz ni aniq chiqaradi
print(math.pi)         # 3.141592653589793
print(math.factorial(5))  # 120


import datetime

hozir = datetime.datetime.now()
print("Hozirgi vaqt:", hozir)

bugun = datetime.date.today()
print("Bugungi sana:", bugun)
def help():
    print("Dastur yoshga qarab turli xabarlar chiqaradi.")
    print("Yoshingizni kiritganingizda, dastur sizga mos xabarni ko'rsatadi.")
    print("Chiqish uchun 'yoq' deb yozing.")