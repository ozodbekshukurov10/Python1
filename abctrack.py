from abc import ABC, abstractmethod

class Electrtarmogi(ABC):
    @abstractmethod
    def tokyondi(self):
        print('tok keldi')
        print('svet yondi')

    def tokkelmadi(self):
        print('tok kelmadi')
        print('svet yonmadi')


class korxona(Electrtarmogi):
    def tokyondi(self):
         super().tokyondi()
    

    def svet(self):
        print('korxonada svet yondi')


class Uy(Electrtarmogi):
    def tokyondi(self):
         super().tokyondi()
    
    def svet(self):
        print('uylarda  svet yondi')


class Tashkilot(Electrtarmogi):
    def tokyondi(self):
         super().tokyondi()

    def svet(self):
        print('tashkilotda svet yondi')


class Qishloq(Electrtarmogi):
    def __init__(self, uylar):
        self.uylar = uylar


    def tokyondi(self):
        print('Qishloqga tok keldi')
        for uy in self.uylar:
            uy.svet()


class Shaxar(Electrtarmogi):
    def __init__(self, tashkilotlar):
        self.tashkilotlar = tashkilotlar


    def tokyondi(self):
        print('shaxarga tok keldi')
        for tashkilot in self.tashkilotlar:
            tashkilot.svet()


uy1 = Uy()
uy2 = Uy()
qishloq = Qishloq([uy1, uy2])


tashkilot1 = Tashkilot()
tashkilot2 = Tashkilot()
shaxar = Shaxar([tashkilot1, tashkilot2])


qishloq.tokyondi()
print()

shaxar.tokyondi()

