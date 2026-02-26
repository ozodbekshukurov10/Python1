def hello_world(n):
    i = 0
    while i < n:
        print('hello')
        i += 1


while True:
    try:
        n = int(input('sonni kiriting: '))
        if n > 0:
            hello_world(n)
        else:
            print('musbat son kiriting')
            continue
    except ValueError:
        print('butun')
        continue



    print('ha/yoq')
    davom = input('davom etamizmi: ').lower()
    if davom == 'yoq':
        print('tugadi')
        break
    elif davom == 'ha':
        continue


