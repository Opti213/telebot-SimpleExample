import telebot
import requests

#enter your own token
bot = telebot.TeleBot('880750397:AAEJs4lqzwjjyuTR1RUVVMdjkVQXwCZpO98')


#buttons
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('hello', 'joke')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, i\'m Viki', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'you can say me: \nhello \njoke')
try:
    @bot.message_handler(content_types=['text'])
    def send_message(message):
        if message.text.lower() == 'hello':
            bot.send_message(message.chat.id, 'Hi <3')
        elif message.text.lower() == 'joke':
            responce = requests.get('http://api.icndb.com/jokes/random')
            bot.send_message(message.chat.id, responce.json()['value']['joke'])
        else:
            bot.send_message(message.chat.id, 'wrong enter, please enter /help')
except Exception as e:
    print(e)

bot.polling()
