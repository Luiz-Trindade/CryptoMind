import telebot
import os
from dotenv import load_dotenv
from crypto_mind import *

load_dotenv()
telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY", "")

help_commands = """
/help       ---> Show availible commands.
/analysis   ---> Show an technical analisys of bitcoin.
"""

try:
    print("O bot está rodando!")
    bot = telebot.TeleBot(telegram_bot_api_key, parse_mode=None)

    @bot.message_handler(commands=["help", "start"])
    def help(message):
        bot.reply_to(message, help_commands)

    @bot.message_handler(commands=["analysis"])
    def analysis(message):
        bot.reply_to(message, crypto_mind_analysis())
    
    bot.infinity_polling()

except Exception as error:
    print(error)
