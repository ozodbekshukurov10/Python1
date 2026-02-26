import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail login ma'lumotlari
sender_email = "ozodbeks805@gmail.com"
password = "ozodbek2010"

# Qabul qiluvchi
receiver_email = "ozodbek201024@gmail.com"

# Xabar mazmuni
subject = "Forward School haqida"
body = "Salom! Forward School bilan 6 oyda ingliz tilini o‘rganing!"

# Xabarni yig'ish
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Gmail serveriga ulanish va xabar yuborish
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Xabar muvaffaqiyatli yuborildi!")
except Exception as e:
    print("Xatolik yuz berdi:", e)
