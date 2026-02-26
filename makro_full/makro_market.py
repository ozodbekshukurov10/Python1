import json


store_file = "makro_storege.json"


data = {
    "ovqatlar": ['osh', 'shashlik', 'somsa', 'lagmon', 'kebab', 'baklava', 'dolma', 'pide'],
    
}


def save_data():
    with open(store_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open(store_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return data

data = load_data()
while True:

    print("                                                              hush kelibsiz                                         ")
    print("mijoz")
    print("makro ishchisi")
    user = input("ozingizni tanishtiring: ").lower()

    menu = ['1 - ozbek taomlari', '2 - turk taomlari']

    if user == "makro ishchisi":
        Name = input("ismingini kiritng: ").lower()
        if Name == "azizbek":
            pasword = input("parolni kiriting: ")
            if pasword == "12345":
                print("xush kelibsiz direktor")
                yangi = input("ishchi qoshish yoki ayrish: ")
                if yangi == "qoshish":
                    print(data["ishchilar"])
                    print()
                    yangi = input("ishchi nomini kiriting: ")
                    data["ishchilar"].append(yangi)
                    save_data()
                    print("ishchi qoshildi",yangi)
                elif yangi == "ayrish":
                    print(data["ishchilar"])
                    print()
                    ayrish = input("qaysi ishchini ayrish: ")
                    if ayrish in data["ishchilar"]:
                        data["ishchilar"].remove(ayrish)
                        save_data()
                        print(f'{ayrish} ishchisi ayrildi')
        elif Name == "lazizbek":
            pasword = input("parolni kiriting: ")
            if pasword == "12345":
                print("xush kelibsiz bosh menejer")
                print("ozbek menu")
                print("turk menu")
                a = input("qaysi menu dan o‘zgartirasiz: ")
                if a == "ozbek menu":
                    print(data["ovqatlar"])
                    print()
                    menusorash = input("qoshish yoki ochirish: ")
                    if menusorash == "qoshish":
                        yangi = input("nimalar qoshamiz: ")
                        data["ovqatlar"].append(yangi)
                    elif menusorash == "ochirish":
                        ochir = input("nimalar ochiramiz: ")
                        if ochir in data["ovqatlar"]:
                            data["ovqatlar"].remove(ochir)
                    save_data()
                elif a == "turk menu":
                    print(data["ovqatlar"])
                    print()
                    menusorash = input("qoshish yoki ochirish: ")
                    if menusorash == "qoshish":
                        yangi = input("nimalar qoshamiz: ")
                        data["ovqatlar"].append(yangi)
                    elif menusorash == "ochirish":
                        ochir = input("nimalar ochiramiz: ")
                        if ochir in data["ovqatlar"]:
                            data["ovqatlar"].remove(ochir)
                            save_data()
    elif user == "mijoz":
        print("xush kelibsiz mijoz")
        print(menu)
        tanlash = input("qaysi birini tanlaysiz: ")
        if tanlash == "1":
            print("ozbek shifr")
            ozbekmenu = ['osh', 'shashlik', 'somsa', 'lagmon']
            print("Menu:", ozbekmenu)
            sorash = input("qaysi taomni tanlaysiz: ")
            print("Siz tanlagan taom:", sorash)
            print("buyurtmalaringiz:", sorash)
            print("Menu:", ozbekmenu)
        elif tanlash == "2": 
            print("turk shifr")
            turkmenu = ['kebab', 'baklava', 'dolma', 'pide']
            print("Menu:", turkmenu)
            sorash2 = input("qaysi taomni tanlaysiz: ")
            print("buyurtmalaringiz:", sorash2)
            print("Menu:", turkmenu)
        else:
            print("notog‘ri tanlov")
