import random

random.Random()

student = {
    'ozodbek': {
    'name': 'ozodbek',
    'age': 16,
    'class': 9,
    'height': 163,
    'weight': 45,
    },
    'xojiakbar': {
    'name': 'xojiakbar',
    'age': 15,
    'class': 8,
    'height': 170,
    'weight': 50,
    },
    'Oyatillo': {
    'name': 'oyatillo',
    'age': 18,
    'class': 11,
    'height': 180,
    'weight': 70,
    }
}


xususiyat = random.choice(list(student.items()))
print(xususiyat)



#one = []

#for i in range(1, 101):
 #   one.append(i)


#two = random.sample(one, len(one))
#print(two)

