class person:
    def __init__(self, olama, shopptoli, gopporalii, dala):
        self.olama = olama
        self.shopptoli = shopptoli
        self.gopporali = gopporalii
        self.dala = dala

    

#bozorlik = input("Bozorlik ni kriting: ")

for i in range(1):
    olama = input('olama ni kiriting: ')
    shopptoli = input('shoptolini kriting: ')
    gopporali = input('goppotali kriting:')
    dala = input('dalani kriting:')

    person1  = person(olama=olama, shopptoli=shopptoli, gopporalii=gopporali, dala=dala)
    print(f'olama: {person1.olama}, shopptoli: {person1.shopptoli}, gopporlai: {person1.gopporali}, dala: {person1.dala}')

