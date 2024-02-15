import telebot
import requests
import get_token
from cbr_data import get_data_from_cbr

films=[]
API_URL='https://7038.deeppavlov.ai/model'
API_URL_Cat='https://7035.deeppavlov.ai/model'

TOKEN = get_token.get_telegram_token()

bot = telebot.TeleBot(TOKEN)

def pr(text, message):
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        pr('Приветствую, \nЯ могу отвечать на ваши запросы:', message)
        pr('/q - отвечу предложением на вопрос.', message)
        pr('/w - определю категорию для вашего запроса.', message)
        pr('/c - вывести актуальный курс USD с сайта ЦБР', message)
        pr('Пример запроса: /w Машины ездят по дорогам', message)

    except:
        pr('Что-то не то', message)

@bot.message_handler(commands=['q'])
def q(message):
    quest = message.text.split()[1:]
    qq=" ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")

@bot.message_handler(commands=['w'])
def q(message):
    quest = message.text.split()[1:]
    qq=" ".join(quest)
    data = { 'x': [qq]}
    try:
        res = requests.post(API_URL_Cat,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")

@bot.message_handler(commands=['c'])
def c(message):
    try:
        res = get_data_from_cbr()
        txt = "Текущий курс USD: " + res
        bot.send_message(message.chat.id, txt)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")

bot.polling()