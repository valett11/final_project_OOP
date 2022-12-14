import json
import requests
import telebot

TOKEN = "5823312097:AAEk7BcZ2dP7zqghFaI5pbwik6eyvsO7BOY"

bot = telebot.TeleBot(TOKEN)
keys = {'биткоин': 'BTC',
        'эфириум': 'ETH',
        'доллар': 'USD',
        'тон': 'TONCOIN'
}
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n\n <имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n\n Увидеть список всех доступных валют команда - /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена{amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()