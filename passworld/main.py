import telebot
import sys
from loguru import logger
from commands import command
from functools import wraps

logger.add("../logs/log", level="TRACE", rotation="1 day", compression="zip")
logger.info("Start logging")

try:
    BOT_TOKEN = sys.argv[1]
except:
    print(
        "USAGE:\n\tpoetry run python3 main.py $(cat ../BOT_TOKEN)\nor\n\t. ./startbot.sh"
    )
logger.info(f"Bot token = {BOT_TOKEN}")

bot = telebot.TeleBot(BOT_TOKEN)


def trace_log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.info(f"start {f.__name__}")
        res = f(*args, **kwargs)
        logger.info(f"end {f.__name__}")
        return res

    return wrapper


@bot.message_handler(commands=["start"])
@trace_log
def start_screen(message):
    text = f"Hello, {message.from_user.username}"
    sent = bot.send_message(message.from_user.id, text)


bot.polling(none_stop=True, interval=0)
