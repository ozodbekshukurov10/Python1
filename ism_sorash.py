import json

names = []
age = []

while True:
    name = input('ismingizni kiriting: ')
    yosh = input('yoshingizni kritjing: ')

    if name == 'stop':
        break

    names.append(name)
    age.append(yosh)

data = {
    'names': names,
    'age': age
}


print(json.dumps(data, indent=4,))    
