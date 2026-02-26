data = ['salom', 'xayr', 12, 33, 222, 777]

while True:
    print('int - int ochirish')
    print('str - str ochirish')
    print('chiqish - chiqish')
    print('list:' ,data)
    print()
    print()
   



    b = input('nimani ochirish kerak:')

    if b == 'chiqish':
        break




    i = 0

    while i <len(data):
        if b == 'int' and type(data[i]) is int:
            data.pop(i)
            continue
        elif b == 'str' and type(data[i]) is str:
            data.pop(i)
            continue
        else:
            i += 1
