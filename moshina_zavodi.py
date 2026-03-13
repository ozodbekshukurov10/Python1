class Sportcar:
    def mersades():
        print('markasi: mersades')
        print('modeli: mag one')
        print('dvigateli: 1.6l v6 + 4 electric motor')
        print('ot kuchi: 1062hp')
        print('max tezlik: 360km/h')


    def bmw():
        print('markasi: bmw')
        print('modeli: m4 cs')
        print('ot kuchi: 510hp')
        print('max tezlik: 320km/h')


class Person:
    def __init__(self, markasi, modeli, dvigateli, ot_kuchi):
        self.markasi = markasi
        self.modeli = modeli
        self.dvigateli = dvigateli
        self.ot_kuchi = ot_kuchi

    def settr(self, markasi, modeli, dvigateli, ot_kuchi):
        self.markasi = markasi
        self.modeli = modeli
        self.dvigateli = dvigateli
        self.ot_kuchi = ot_kuchi

    def gettr(self):
        return self.markasi, self.modeli, self.dvigateli, self.ot_kuchi

class Mashina(Person):
    def __init__(self, markasi, modeli, dvigateli, ot_kuchi, tezlik):
        super().__init__(markasi, modeli, dvigateli, ot_kuchi)
        self.tezlik = tezlik


    def gettr(self):
        kengayish = super().gettr()
        return kengayish + (self.tezlik,)
    

l = Mashina('Mersades', 'amg one', '1.6l v6 + 4 electrric motor', '1062hp', '360hm/h')
print(l.gettr())


print()
Sportcar.mersades()
print()
Sportcar.bmw()