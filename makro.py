a = int(input("PIN kod kiriting: ").strip())

abirinchidaraja = 1111
aikkinchidaraja = 2222

if a == abirinchidaraja:
    print("1-daraja")

    son = int(input("Son: "))
    daraja = int(input("Daraja: "))
    natija = son ** daraja
    print(f"Natija: {natija}")

elif a == aikkinchidaraja:
    print("2-daraja")

    son = int(input("Son: "))
    son2 = int(input("Son2: "))
    natija = son + son2
    print(f"Natija: {natija}")

else:
    print("Boshqa daraja")
