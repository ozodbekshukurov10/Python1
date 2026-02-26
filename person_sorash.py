import json
import os

filename = "baza.json"


if not os.path.exists(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([], f)


def load_data():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        save_data([])
        return []

    
def save_data(data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_person():
    people = load_data()
    name = input('ism: ')
    familiya = input('familiya: ')
    age = input('yosh: ')
    person = {
        'name': name,
        'familiya': familiya,
        'age': age
    }
    people.append(person)
    save_data(people)
    print(f'{name} {familiya} qoshildi')


def show_all():
    people = load_data()
    print('Baza dagi odamlar')
    print(json.dumps(people, indent=4, ensure_ascii=False))


def srearch_person(name):
    people = load_data()
    for p in people:
        if p["name"].lower() == name.lower():
            chiqarish = input(f"{name} topildi. Ma'lumotlar chiqarilsinmi? (ha/yo'q): ")
            if chiqarish == 'ha':
                print(f'ism: {p["name"]}\nfamiliya: {p["familiya"]}\nyosh: {p["age"]}')
            else:
                print('xatolik yuz berdi')
                return


while True:
    print('1. Odam qo\'shish')
    print('2. Baza dagi odamlarni ko\'rish')
    print('3. Odam qidirish')
    print('4. Chiqish')
    sorash = input('buruq: ')
    if sorash == '1':
        add_person()
    elif sorash == '2':
        show_all()
    elif sorash == '3':
        name = input('qidiriladigan odamning ismini kiriting: ')
        srearch_person(name)
    elif sorash == '4':
        print('dasturdan chiqish')
        break
