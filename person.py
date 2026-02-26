import random

foydalanuvchilar = ["shokir", "hasan", "aziz", "alisher"]

javoblar = {
    "salom": ["Va alaykum assalom!", "Salom "],
    "qachon": ["Tez orada aytaman.", "Hozir aniqlashtiryapman."],
    "qarz": ["Qarzni yaqin orada beraman.", "Iltimos sabr qiling."],
    "qalesan": ["Yaxshiman, rahmat!", "Yuribmiz "],
    "qayerdasan": ["hozir lokatsiya tahlayman"],
}

yuboruvchi = input("Kimdan: ").lower()
xabar = input("Xabar: ").lower()


unli_bormi = False
for harf in "aeiouo'":
    if harf in xabar:
        unli_bormi = True

kimga = "Noma'lum"
for ism in foydalanuvchilar:
    if ism in xabar and ism != yuboruvchi:
        kimga = ism.capitalize()

if unli_bormi == False or len(xabar) < 3:
    javob = "Iltimos, to'g'ri yozing, tushunarsiz xabar yubordingiz! ⚠️"
else:
    javob = "Xabaringiz qabul qilindi." # Standart javob
    for kalit_soz in javoblar:
        if kalit_soz in xabar:
            javob = random.choice(javoblar[kalit_soz])
            break

print("-" * 20)
print(f"Kimga: {kimga}")
print(f"Bot javobi: {javob}")
