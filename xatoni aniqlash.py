print('menga bugun dam')

print('1 - Qoshish')
print('2 - Ayirish')
print('3 - Kopaytirish')
print('4 - Bolish')
print('5 - Darajaga kopaytirish')
print('6 - Daraja hisoblash')


import webbrowser

cod_1 = 2222

a = int(input("amaldi kiriting: "))
b = int(input("1-sonni kiriting: "))
c = int(input("2-sonni kiriting: "))


if b + c == cod_1:
    webbrowser.open('https://www.youtube.com/')
elif a == 1:
    print(b + c)
elif a == 2:
    print(b - c)
elif a == 3:
    print(b * c)
elif a == 4:
    print(b / c)
elif a == 5:
    print(b ** c)
elif a == 6:
    print(b ** (1/c))

else:
    print('erorr')
