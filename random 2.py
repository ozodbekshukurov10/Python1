import random

frends_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]

isimlar = random.sample(frends_names, 4)
print(isimlar)



one = []

for i in range(1, 101):
    one.append(i)



two = random.sample(one, len(one))
print(two)