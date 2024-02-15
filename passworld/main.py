import telebot
import sys
from loguru import logger as log
from commands import command
from functools import wraps
from keyboards import start_screen_keyboard, test_kb
import messages

log.remove()
log.add(sys.stdout, level="TRACE")

log.add("../logs/{time}.log", level="TRACE", rotation="1 day", compression="zip")
log.info("Start logging")

try:
    BOT_TOKEN = sys.argv[1]
except:
    print(
        "USAGE:\n\tpoetry run python3 main.py $(cat ../BOT_TOKEN)\nor\n\t. ./startbot.sh"
    )
log.info(f"Bot token = {BOT_TOKEN}")

bot = telebot.TeleBot(BOT_TOKEN)


def trace_log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        log.trace(f"start {wrapper.__name__}")
        res = f(*args, **kwargs)
        log.trace(f"end {wrapper.__name__}")
        return res

    return wrapper


@bot.message_handler(commands=["start"])
@trace_log
def start_screen(message):
    sent = bot.send_message(message.from_user.id,
                            messages.start_screen_message(),
                            reply_markup=start_screen_keyboard)

bot.polling(none_stop=True, interval=0)
