import telebot
import os
from dotenv import load_dotenv
from crypto_mind import *

load_dotenv()
telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY", "")

help_commands = """
COMMANDS:

/help       ---> Display available commands.
/bitcoin    ---> Get Bitcoin (BTC) analysis.
/ethereum   ---> Get Ethereum (ETH) analysis.
/binance    ---> Get Binance Coin (BNB) analysis.
/xrp        ---> Get XRP analysis.
/cardano    ---> Get Cardano (ADA) analysis.
/solana     ---> Get Solana (SOL) analysis.
/dogecoin   ---> Get Dogecoin (DOGE) analysis.

🤖 *About CryptoMind*  
CryptoMind is a technical analysis bot that helps you make informed decisions when trading cryptocurrencies.  

👨‍💻 *Creator:* [Luiz Gabriel Magalhães Trindade](https://github.com/Luiz-Trindade)  
📂 *GitHub Repository:* [CryptoMind](https://github.com/Luiz-Trindade/CryptoMind)  
"""

try:
    print("O bot está rodando!")
    bot = telebot.TeleBot(telegram_bot_api_key, parse_mode=None)

    @bot.message_handler(commands=["help", "start"])
    def help(message):
        bot.reply_to(message, help_commands)

    @bot.message_handler(commands=["bitcoin"])
    def bitcoin(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="BTC-USD", periodo="6mo"))

    @bot.message_handler(commands=["ethereum"])
    def ethereum(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="ETH-USD", periodo="6mo"))

    @bot.message_handler(commands=["binance"])
    def binance(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="BNB-USD", periodo="6mo"))

    @bot.message_handler(commands=["xrp"])
    def xrp(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="XRP-USD", periodo="6mo"))

    @bot.message_handler(commands=["cardano"])
    def cardano(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="ADA-USD", periodo="6mo"))

    @bot.message_handler(commands=["solana"])
    def solana(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="SOL-USD", periodo="6mo"))

    @bot.message_handler(commands=["dogecoin"])
    def dogecoin(message):
        bot.reply_to(message, crypto_mind_analysis(ticker="DOGE-USD", periodo="6mo"))

    bot.infinity_polling()

except Exception as error:
    print(error)
