from telebot import types
from commands import command

start_screen_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

btns = []

for cmd in command:
    btns.append(types.KeyboardButton(cmd.text))

start_screen_keyboard.add(*btns)
