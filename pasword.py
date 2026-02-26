x = int(input("codi kiriting: "))

password1 = 1234
password2 = 5678
password3 = 91011

if x == password1:
    print("1-daraja")

    cod = int(input("cod kriting: "))
    codasli = 1111
    print(cod == codasli and "kirtingiz")
    input_value = int(input("Son: "))
    power_value = int(input("Daraja: "))
    result = input_value ** power_value
    print(f"Natija: {result}")

elif x == password2:
    print("2-daraja")

    cod = int(input("cod kriting: "))
    codasli = 2222
    print(cod == codasli and "kirtingiz")
    print("2-daraja")

    input_value1 = int(input("Son: "))
    input_value2 = int(input("Son2: "))
    result = input_value1 + input_value2
    print(f"Natija: {result}")

elif x == password3:
    print("3-daraja")

    cod = int(input("cod kriting: "))
    codasli = 3333
    print(cod == codasli and "kirtingiz")

    input_value1 = int(input("boyizi kiriting: "))
    input_value2 = int(input("kilogramizi kiriting: "))
    boy = input_value1 * 2
    bmi = input_value1 / input_value2
    print(f"Sizning BMI: {bmi:.2f}")