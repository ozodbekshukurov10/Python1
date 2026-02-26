sonlar = [12, 42, 22, 84, 1,58,35,70,1,55,777,999,625,2,67,76,7075,6065]

sonlar.sort()

son = sonlar.index(35)

son_1 = (sonlar[son + 5])
son_2 = (sonlar[son - 3])

print(son_1 * son_2)