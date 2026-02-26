person = {
    "name": "ali",
    "age": 16,
    "weight": 45,
    "height": 165,
    "hobby": ["football", "programming", "reading"],
    "adress": {
        "city": "Andijon",},
    "gender": True,
}

person["job"] = "student"  # yangi kalit va qiymat qo'shish
person["age"] = 17  # mavjud kalitning qiymatini o'zgartirish
del person["weight"]  # kalit va uning qiymatini o'chirish
person.pop("height")  # kalit va uning qiymatini o'chirish va qiymatini qaytarish

print(person['adress']['city'],person['hobby'][1])  # nested dictionary va ro'yxatga murojaat qilish
