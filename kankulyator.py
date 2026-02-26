# Kankulyator
x = input("operatorni kiriting (+, -, *, /): ")
number_1 = int(input("birinchi raqamni kiriting: "))
number_2 = int(input("ikkinchi raqamni kiriting: "))

if x == "+":
    print("Natija:", number_1 + number_2)
elif x == "-":
    print("Natija:", number_1 - number_2)
elif x == "*":
    print("Natija:", number_1 * number_2)
elif x == "/":
    if number_2 != 0:
        print(f"{number_1}/{number_2}/={number_1 / number_2}")

        
        print("Natija:", number_1 / number_2)
    else:
        print("xatolik bor")