import telebot
import os
from dotenv import load_dotenv
from crypto_mind import *

load_dotenv()
telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY", "")

help_commands = """
COMMANDS:

/help       ---> Display available commands.
/analysis   ---> Perform a technical analysis of Bitcoin.

🤖 *About CryptoMind*  
CryptoMind is a technical analysis bot that helps you make informed decisions when trading Bitcoin.  

👨‍💻 *Creator:* [Luiz Gabriel Magalhães Trindade](https://github.com/Luiz-Trindade)  
📂 *GitHub Repository:* [CryptoMind](https://github.com/Luiz-Trindade/CryptoMind)  
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
