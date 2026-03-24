a = input('1-ishchi yoki 2-oquvchi: ')

def ishchilar():
    print('Abduraxmon')
    print('Abdullo')
    print('Abubakir')

def kurslar():
    print('web dasturlash')
    print('mobil dasturlash')
    print('grafik dizayn')
    print('office pro')
    print('kiberxavsizlik')

def weboquvchilari():
    print('davron')
    print('sarvinoz')




if a == '1':
    print('ishchi bolib kridingiz')
    ishchilar()
    b = input('kim siz: ')
    if b == 'Abduraxmon':
        print('siz bosh menejersiz')
        print('kurslar')
        kurslar()
        print('kursdan tanlang u ni ichida kimlar borligi korsaadi')
        print('1-web dasturlash')
        print('2-mobil dasturlash')
        print('3-grafik duzayn')
        print('4-office pro')
        print('5-kiberxavsizlik')
    elif b == 'ismoil':
        print('siz bugeltersiz')
        sorash = input('qaysi kursdi tanlaysiz: ')
        if sorash == '1':
            print('web dasturlash oquvchilar')
            sorash2 = input('qaysi guruppa: ')
            print('1-9 guruuppalar')
            if sorash2 == '1':
                print('abdulloh')
                print('lola')
                print('iskandar')
            elif sorash2 == '2':
                print("mohigul")
                print("samandar")
            