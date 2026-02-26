# xavfsiz_voice_assistant.py
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import getpass

engine = pyttsx3.init()
r = sr.Recognizer()

# Oq-ro'yxat: faqat shu amallar bajariladi
WHITELIST = {
    "google": lambda: webbrowser.open("https://google.com"),
    "youtube": lambda: webbrowser.open("https://youtube.com"),
    "kalkulyator": lambda: os.system("calc"),
    "bloknot": lambda: os.system("notepad"),
    "music": lambda: print("Musiqa ochish bu yerda sozlanadi (misol)"),
}

# Maxsus sezgir buyruqlar (parol + tasdiq talab qiladi)
SENSITIVE = {
    "shutdown": lambda: os.system("shutdown /s /t 5"),  # izoh: xavfli -> default izohlarga o'girildi
}

# Boshlashda konsoldan parol oling (mahalliy egasi uchun)
OWNER_PASSWORD = getpass.getpass("Iltimos — yordamchi parolini kiriting (mahalliy kompyuter egasi uchun): ")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command(timeout=5):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Gapiring... ({}s ichida)".format(timeout))
        audio = r.listen(source, timeout=timeout, phrase_time_limit=6)
    try:
        text = r.recognize_google(audio, language="uz-UZ").lower()
        print("Tanish natija:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Internetga ulanmaganman, ovoz tanib bo'lmadi")
        return ""

def require_password():
    # ekranda parol tekshiruvi — ovoz orqali parol qabul qilish xavfsiz emas
    attempt = getpass.getpass("Parolni kiriting: ")
    return attempt == OWNER_PASSWORD

def main_loop():
    speak("Xavfsiz yordamchi ishga tushdi")
    while True:
        text = listen_command()
        if not text:
            speak("Tushunmadim, qayta ayt")
            continue

        if "chiq" in text or "tugadi" in text or "stop" in text:
            speak("Yordamchi to'xtadi")
            break

        # Sensitiv buyruqlar
        for key in SENSITIVE:
            if key in text:
                speak(f"{key} buyruq aniqlangan. Tasdiqlash va parol kerak.")
                if require_password():
                    speak("Parol to'g'ri. Iltimos, yozma tasdiqni kiriting (ha/yo'q).")
                    confirm = input("Tasdiqlaysizmi? (ha/yo'q): ").strip().lower()
                    if confirm == "ha":
                        speak(f"{key} bajarilmoqda")
                        # Eslatma: xavfli amallarni faollashtirishdan oldin izohni olib tashlang
                        SENSITIVE[key]()  # agar xavfli bo'lsa - ogohlantirish bilan
                    else:
                        speak("Bekor qilindi")
                else:
                    speak("Parol noto'g'ri. Bekor qilindi.")
                break
        else:
            # Whitelist buyruqlar
            matched = False
            for key in WHITELIST:
                if key in text:
                    matched = True
                    speak(f"{key} ochilmoqda")
                    WHITELIST[key]()
                    break
            if not matched:
                speak("Bu buyruq ro'yxatda yo'q yoki ruxsatsiz. Iltimos faqat qonuniy va xavfsiz buyruqlar bering.")

if __name__ == "__main__":
    main_loop()
