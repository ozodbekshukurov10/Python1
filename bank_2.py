import json

fayk = 'bank_2.json'


class bank:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans


    def pul_qoshish(self, summa):
        if summa >= 0:
            self.balans += summa
            print('pul qoshildi')
        else:
            print('notogi summa')


    def pul_yechish(self, summa):
        if 0 < summa <= self.balans:
            self.balans -= summa
            print('pul yechildi')
        else:
            print('yetarli mablag yoq')
    

    def __str__(self):
        return f'{self.egasi} | balans: {self.balans}'
    

def yuklash():
    try:
        with open(fayl, 'r') as f:
            data = json.load(f)
            return{k: bank(k, v) for k, v in data.items()}
    except FileExistsError:
        return {}
    
def yuklash(hisoblar):
    data = {k: v.balans for k, v in hisoblar.items()}
    with open(fayl, 'w') as f:
        json.dump(data, f, indent=4)


hissoblar = yuklash()


while True:
    print('1. yangi hisob yaratish')
    print('2. pul qoshish')
    print('3. pul yechish')
    print('4. hisoblar korish')
    print('5. chiqish')


    tanlov = input('tanlovsi kiriting: ')


    if tanlov == '1':
        ism = input('ism kiriting')
        boshlangich = int(input('boshlangich balans: '))
        hissoblar[ism] = bank(ism, boshlangich)
        saqlash(hissoblar)
        print('hisoblar yaratildi')

    elif tanlov == '2':
        ism = input('qaysi hisobga: ')
        if ism in hissoblar:
            summa = int(input('summa: '))
            hissoblar[ism].pul_yeshish(summa)
            saqlash(hissoblar)
        else:
            print('bunday hisob yoq')
    elif tanlov == '4':
        for hisob in hissoblar.values():
            print('hisob')
    
    elif tanlov == '5':
        break

    else:
        print('notogri tanlov')
