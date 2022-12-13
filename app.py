import telebot

TOKEN = "5823312097:AAEk7BcZ2dP7zqghFaI5pbwik6eyvsO7BOY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message:telebot.types.Message):
    bot.send_message(message.chat.id, "hello")

bot.polling()