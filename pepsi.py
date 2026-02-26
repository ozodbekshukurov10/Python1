a= 'assalomu alaykum'

print(a.center(150))


login = input('loginingizni kiriting: ')
password = input('parolingizni kiriting: ')

login_asli = 'admin'
password_asli = '2323'

login_asli2 = 'user'
password_asli2 = '123456'



parol_asli = 0000
parol_asli2 = 1111


buyurtmalar = []

if login == login_asli and password == password_asli:
    print('Xush kelibsiz ishchi')
    print('Bosh menejer')
    menu = ['fanta', 'coca cola']
    qoshish = 'qoshish'
    ayrish = 'ayrish'
    print('hozirgi menu:', menu)
    print('A - qoshish')
    print('B - ochirish')
    sorov2 = input('menuga qanday ozagartish kiritish kerak? ')
else:
    print('Xato login yoki parol')
    exit()
if sorov2 == 'A':
        menu.append(input('qanday mahsulot qoshmoqchisiz? '))
elif sorov2 == 'B':
        menu.remove(input('qanday mahsulotni ochirmoqchisiz? '))

print('Yangi menu:', menu)



b = input('login: ')
d = input('password: ')

if b == login_asli2 and d == password_asli2:
        print('xush kelibsiz mijoz')
        print(menu)
        buyurtma = input('nima buyurtma berasiz: ')
        buyurtmalar.append(buyurtma)
        print('bizni tanlaganiz uchun raxmat')
        print(buyurtmalar)
        exit()
else:
    print('Xato login yoki parol')
