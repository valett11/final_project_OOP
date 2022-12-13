import telebot

TOKEN = "5823312097:AAEk7BcZ2dP7zqghFaI5pbwik6eyvsO7BOY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n <имя валюты> \
    <в какую валюту перевести>\
    <количество переводимой валюты>"
    bot.reply_to(message, text)

bot.polling()