data_type =  ['salom', 12, 4.5, True, False, [1, 2, 3], (4, 5), 'xayr', 99, 3.5, 222, 777, 555, ]


ints = []
floats = []
strs = []
bools = []
lists = []
tuples = []

i = 0



while i < len(data_type):
    item = data_type[i]

    if type(item) is bool:
        bools.append(item)
    elif type(item) is int:
        ints.append(item)
    elif type(item) is float:
        floats.append(item)
    elif type(item) is str:
        strs.append(item)
    elif type(item) is list:
        lists.append(item)
    elif type(item) is tuple:
        tuples.append(item)

    i += 1

listlar = {'int': ints, 'float': floats, 'str': strs, 'bool': bools, 'list': lists, 'tuple': tuples}


while True:
    print('lype turini kiriting')
    print('int', 'str', 'float', 'bool', 'list', 'tuple')
    print('chiqish')
    tanlagn = input('type turini kiriting: ').lower()


    if tanlagn == 'chiqish':
        print('chqish')
        break
    elif tanlagn in listlar:
        print(f'\n{tanlagn}:')
        print(listlar[tanlagn])
        print()
        print()
    else:
        print('notogri')
