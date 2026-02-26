from twilio.rest import Client

# Twilio hisob ma'lumotlari
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
client = Client(account_sid, auth_token)

# SMS yuborish
message = client.messages.create(
    body="Salom Ozodbek! Forward School bilan 6 oyda ingliz tilini o‘rganing!",
    from_="+1234567890",   # Twilio'dan olingan raqam
    to="+998903822210"     # Sizning raqamingiz (90 382 22 10)
)

print("SMS yuborildi:", message.sid)
