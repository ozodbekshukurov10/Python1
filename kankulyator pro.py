amal = input("qanday amal bajarilsin (daraja =1) or (kankulyatsiya = 2) ? : ")

if amal == "1":
    k = input("kvadrat uchun 1. kub uchun 2 ni bosing : ")
    number = int(input("son kiriting: "))
    if k == "1":
        o = number ** 2
        print(f"{number} ning kvadrati {o}")
    elif k == "2":
        e = number ** 3
        print(f"{number} ning kubi {e}")
    else:
        print("error")
elif amal == "2":
    operator = input("operatorni kiriting")
    number1 = int(input("birinchi raqamdi kiriting : "))
    number2 = int(input("ikkinchi raqamdi kiriting : "))

    if operator == "+":
        a = number1 + number2
        print(f"{number1} + {number2} = {a}")
    elif operator == "-":
        b = number1 - number2
        print(f"{number1} - {number2} = {b}")
    elif operator == "*":
        c = number1 * number2
        print(f"{number1} * {number2} = {c}")
    elif operator == "/":
        d = number1 / number2
        print(f"{number1} / {number2} = {d}")
    else:
        print("Error")

        
