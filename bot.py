import telebot
from telebot import types
import requests
from configuration.config import tg_token
from random import randint

bot = telebot.TeleBot(tg_token)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Числа (математика)", callback_data='num_math')
    btn2 = types.InlineKeyboardButton("Просто числа", callback_data='num_simple')
    btn3 = types.InlineKeyboardButton("Даты", callback_data='date')
    keyboard.row(btn1)
    keyboard.row(btn2, btn3)

    bot.send_message(message.chat.id, "Привет! Я бот, который будет давайть вам интересные факты о числах и датах (не всегда))", reply_markup=keyboard, )
    bot.register_next_step_handler(message, answer)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Числа (математика)", callback_data='num_math')
    btn2 = types.InlineKeyboardButton("Просто числа", callback_data='num_simple')
    btn3 = types.InlineKeyboardButton("Даты", callback_data='date')
    keyboard.row(btn1)
    keyboard.row(btn2, btn3)

    if call.data == 'num_math':
        ans = requests.get(f'http://numbersapi.com/random/math')
        bot.send_message(call.message.chat.id, ans.text, reply_markup=keyboard)
    elif call.data == 'num_simple':
        ans = requests.get(f'http://numbersapi.com/random/trivia')
        bot.send_message(call.message.chat.id, ans.text, reply_markup=keyboard)
    elif call.data == 'date':
        ans = requests.get(f'http://numbersapi.com/random/date')
        bot.send_message(call.message.chat.id, ans.text, reply_markup=keyboard)



bot.polling(none_stop=True)