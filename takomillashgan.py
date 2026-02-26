import json
import os
import random

filename = "users.json"
def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except:
                data = []
    else:
        data = []
    return data
if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
        except:
            data = []
else:
    data = []
def add_user(): 
    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    yosh = input('yoshingizni kriting:')
    boy = input('boyingizni kriting: ')
    vazn = input('vazningizni kriting: ')
    uy_manzili = input('uy manzilingizni kriting: ')

    new_user = {
        'ism': ism,
        'familiya': familiya,
        'yosh': yosh,
        'boy': boy,
        'vazn': vazn,
        'uy_manzili': uy_manzili
    }

    data = load_data()
    data.append(new_user)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print('malumotlar saqlandi')

def random_user():
    data = load_data()
    if data:
        tanlangan_user = random.choice(data)
        print("Random tanlangan foydalanuvchi:")
        print(tanlangan_user)
    else:
        print("Foydalanuvchilar ro'yxati bo'sh.")


def main():
    print('1 - jsonga yangi user qoshish')
    print('2 - jsondan random user tanlash')
    tanlov = input('tanlovni kiriting: ')

    if tanlov == '1':
        add_user()
    elif tanlov == '2':
        random_user()
    else:
        print('notogri')
    
main()   