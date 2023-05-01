import telebot
import environ

env = environ.Env()
environ.Env.read_env()

TOKEN = env("BOT_API_KEY")
CHAT_ID = env("CHAT_ID")
BOT_ID = env("BOT_ID")
bot = telebot.TeleBot(TOKEN)


def make_text_for_sending(time, name, phone, city, street, house, apartment, description):
    return f"Заявка від {str(time)[:19]},\n Клієнт: {name}, {phone}, \n Адреса: м.{city}, {street} {house}, кв.{apartment}, \n Опис: {description}"


import requests


def send_telegram_message(message):
    apiURL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': CHAT_ID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
