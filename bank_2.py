import json
import os

fayl = 'bank_2.json'

class Bank:
    def __init__(self, name, last_name, age, balans=0):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.balans = balans

    def pul_qoshish(self, summa):
        if summa >= 0:
            self.balans += summa
            print('Pul qo‘shildi')
        else:
            print('Noto‘g‘ri summa')

    def pul_yechish(self, summa):
        if 0 < summa <= self.balans:
            self.balans -= summa
            print('Pul yechildi')
        else:
            print('Yetarli mablag‘ yo‘q')

    def __str__(self):
        return f'{self.name} {self.last_name} | age: {self.age} | balans: {self.balans}'




def yuklash():
    if not os.path.exists("hisoblar.json"):
        with open("hisoblar.json", "w") as f:
            json.dump({}, f)  # bo‘sh lug‘at yoziladi
    with open("hisoblar.json", "r") as f:
        data = json.load(f)
    hisoblar = {}
    for k, v in data.items():
        hisoblar[k] = Bank(v["name"], v["last_name"], v["age"], v["balans"])
    return hisoblar


def saqlash(hisoblar):
    data = {
        k: {
            "name": v.name,
            "last_name": v.last_name,
            "age": v.age,
            "balans": v.balans
        }
        for k, v in hisoblar.items()
    }
    with open(fayl, 'w') as f:
        json.dump(data, f, indent=4)


def buble_sort(items, key):
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if getattr(items[j], key) > getattr(items[j + 1], key):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def balans_sort(hisoblar):
    items = list(hisoblar.values())
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].balans < items[j + 1].balans:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


hisoblar = yuklash()

while True:
    print('1. Yangi hisob yaratish')
    print('2. Pul qo‘shish')
    print('3. Pul yechish')
    print('4. Hisoblarni ko‘rish')
    print('5. Ism bo‘yicha qidirish')
    print('6. Chiqish')
    print('7. Balans bo‘yicha sort')
    print('8. Filter')

    tanlov = input('Tanlovni kiriting: ')

    if tanlov == '1':
        ism = input('Ism kiriting: ')
        familiya = input('Familiya kiriting: ')
        yosh = int(input('Yosh kiriting: '))
        boshlangich = int(input('Boshlang‘ich balans: '))
        hisoblar[ism] = Bank(ism, familiya, yosh, boshlangich)
        saqlash(hisoblar)
        print('Hisob yaratildi')

    elif tanlov == '8':
        print('1 - Yosh bo‘yicha')
        print('2 - Ism bo‘yicha')
        sor = input('Tanlov: ')
        if sor == '1':
            results = buble_sort(list(hisoblar.values()), 'age')
            results.reverse()
        elif sor == '2':
            results = buble_sort(list(hisoblar.values()), 'name')
        else:
            print('Xato tanlov')
            results = []
        if results:
            for r in results:
                print(r)
        else:
            print('Topilmadi')

    elif tanlov == '2':
        ism = input('Qaysi hisobga: ')
        if ism in hisoblar:
            summa = int(input('Summa: '))
            hisoblar[ism].pul_qoshish(summa)
            saqlash(hisoblar)
        else:
            print('Bunday hisob yo‘q')

    elif tanlov == '3':
        ism = input('Qaysi hisobdan: ')
        if ism in hisoblar:
            summa = int(input('Summa: '))
            hisoblar[ism].pul_yechish(summa)
            saqlash(hisoblar)
        else:
            print('Bunday hisob yo‘q')

    elif tanlov == '4':
        for hisob in hisoblar.values():
            print(hisob)

    elif tanlov == '5':
        ism = input('Qidirilayotgan ism: ')
        if ism in hisoblar:
            print(hisoblar[ism])
        else:
            print('Bunday ismli hisob topilmadi')

    elif tanlov == '7':
        sorted_hisoblar = balans_sort(hisoblar)
        for h in sorted_hisoblar:
            print(h)

    elif tanlov == '6':
        break

    else:
        print('Noto‘g‘ri tanlov')
