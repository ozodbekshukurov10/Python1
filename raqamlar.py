
start = int(input("Boshlanish raqamini kiriting: "))

end = int(input("Tugash raqamini kiriting: "))


print("1 - Toq raqamlar yig'indisi")
print("2 - Juft raqamlar yig'indisi")
tanlov = int(input("Qaysi birini hisoblaysiz (1 yoki 2): "))


print("\nA - Natijaning o'zi")
print("B - Natijaning kvadrati")
print("C - Natijaning kubi")
korinish = input("Qaysi ko‘rinishni istaysiz:  ").upper()


toq = 0
juft = 0


for i in range(start, end + 1):
    if i % 2 == 0:
        juft += i
    else:
        toq += i


if tanlov == 1:
    natija = toq
    nom = "Toq raqamlar yig'indisi"
elif tanlov == 2:
    natija = juft
    nom = "Juft raqamlar yig'indisi"
else:
    print("Noto‘g‘ri tanlov!")
    exit()


if korinish == "A":
    final = natija
elif korinish == "B":
    final = natija ** 2
elif korinish == "C":
    final = natija ** 3
else:
    print("Noto‘g‘ri tanlov!")
    exit()


print(f"\n{nom}: {final}")
