import json
import os


filename = 'bank.json'

class bank:
    def __init__(self, kartaraqami, balans):
        self.kartaraqami = kartaraqami
        self.balans = balans

    def tekshirish(self, kiritilgan_balans):
        if self.balans == kiritilgan_balans:
            print('karta sizniki')
            return True
        else:
            print('karta ogirlangan')
            return False
    def pul_qoshish(self, summa):
        self.balans += summa
        print(f'{summa} som qoshildi. balans {self.balans}')
        self.saqlash('qohish', summa)

    def pul_ayrish(self, summa):
        if self.balans >= summa:
            self.balans -= summa
            print(f'{summa} som ayrildi. balans {self.balans}')
            self.saqlash('ayrish', summa)
        else:
            print('xatolik yuz berdi')

    def saqlash(self, amal, summa):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = []

        data.append({'kartaraqami':
                   self.kartaraqami,
                     'amal': amal,
                     'summa':summa,
                     'yakuniy_balans': self.balans})
        
        with open(filename, 'w', encoding='utf-8' ) as f:
            json.dump(data, f, indent=4, ensure_ascii=False)



kartaraqami = int(input('karta raqamini kiriting: '))

kiritilgan_balans = int(input('balansdi kiriting: '))

bank = bank(kartaraqami, 18000000)

if bank.tekshirish(kiritilgan_balans):

    amal = input('qoshish yoki ayrish: ').lower()
    summa = int(input('summa kiriting: '))

    if amal == 'qoshish':
        bank.pul_qoshish(summa)
    elif amal == 'ayrish':
        bank.pul_ayrish(summa)
    else:
        print('error')
