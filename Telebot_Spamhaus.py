import telebot
from spam_lists import SPAMHAUS_DBL
token = "Telebot Api Tokeniniz"
group="Mesaj Göndermeniz Gereken Grubun Adı"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.reply_to(message, "Merhabalar!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    deger = message.text in SPAMHAUS_DBL
    try:
        if(deger):
            bot.send_message(group,"Belirttiginiz url spam listesinde yer almaktadir")
        else:
            bot.send_message(group,"Belirttiginiz url spam listesinde yer almamaktadır")
    except:
        pass
bot.polling()
            