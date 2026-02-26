
birinchi_malumot = int(input('birinchi malumotni kiriting: '))
ikkinchi_malumot = int(input('ikkinchi malumotni kiriting: '))
uchinchi_malumot = int(input('uchunchi malumotni kiriting: '))

birinchi_malumot_asli = 31
ikkinchi_malumot_asli = 21
uchinchi_malumot_asli = 11

if (birinchi_malumot == birinchi_malumot_asli and 
    ikkinchi_malumot == ikkinchi_malumot_asli and 
    uchinchi_malumot == uchinchi_malumot_asli):

    print("Tabriklaymiz")

    print("1 Daraja")
    print("2 BMI hisoblash")
    print("3 Kankulyator")

    tanlov = int(input("Tanlovingiz: "))

    if tanlov == 1:
        son = int(input("Son: "))
        daraja = int(input("Daraja: "))
        natija = son ** daraja
        print(f"Natija: {natija}")

    elif tanlov == 2:
        boy = float(input("Bo'yingiz: "))
        vazn = float(input("Vazningiz: "))

        bmi = vazn / (boy * boy)
        print(f"Sizning BMI: {bmi:.2f}")

        if bmi < 18.5:
            print(" Ozg'in")
        elif 18.5 <= bmi < 25:
            print(" Normal")
        elif 25 <= bmi < 30:
            print(" semiz")
        else:
            print(" juda semiz")

    elif tanlov == 3:
        print("    Kalkulyator ishga tushdi!")
        print("Amallar")
        print("+ ")
        print("- ")
        print("* ")
        print("/ ")

        amal = input("Amalni kiriting: ")
        a = float(input("1-sonni kiriting: "))
        b = float(input("2-sonni kiriting: "))

        if amal == "+":
            print("Natija:", a + b)
        elif amal == "-":
            print("Natija:", a - b)
        elif amal == "*":
            print("Natija:", a * b)
        elif amal == "/":
            if b != 0:
                print("Natija:", a / b)
        else:
            print("error")
    else:
        print("error")



elif birinchi_malumot == 52 and ikkinchi_malumot == ikkinchi_malumot_asli and uchinchi_malumot == uchinchi_malumot_asli:
    print("Tabriklaymiz!")  

else:
    print("Error")
