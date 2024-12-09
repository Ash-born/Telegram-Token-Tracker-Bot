import logging
from telegram.ext import *
from threading import Thread

import requests
import time

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Host': 'fegex-v2-api.fegex.com',
    'If-None-Match': 'W/"9074-qV6JsmJQxSSHaOrc//ChUAeH6pY"',
    'Origin': 'https://beta.fegex.com',
    'Referer': 'https://beta.fegex.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}


def get_transaction(update,tipe):
    while True:

        time.sleep(5)
        if tipe == "rmt":
            link = "https://fegex-v2-api.fegex.com/transactions?id=RUGMUNCHERTOKENfBNB-bsc-dc"
        else:
            link = "https://fegex-v2-api.fegex.com/transactions?id=LOTTERYfBNB-bsc-bf"
        req = requests.get(link, headers=headers)
        old_transactions = req.json()
        time.sleep(60)
        req = requests.get(link, headers=headers)
        new_transaction = req.json()
        for i in range(min(len(old_transactions), len(new_transaction))):
            if new_transaction[i] in old_transactions:
                continue
            else:

                new_buy = new_transaction[i]
                update.message.reply_text(
                    f"""RUGMUNCHERTOKEN Bot found a {new_transaction[i].get("method")} on FEGex of RMT\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n For total of {new_buy.get('transactionPriceUSD')}$""")


def get_buy_transaction(update,tipe):
    while True:
        time.sleep(5)

        if tipe == "rmt" :
            link = "https://fegex-v2-api.fegex.com/transactions?id=RUGMUNCHERTOKENfBNB-bsc-dc"
        else :
            link = "https://fegex-v2-api.fegex.com/transactions?id=LOTTERYfBNB-bsc-bf"
        req = requests.get(link, headers=headers)
        old_transactions = req.json()
        time.sleep(60)
        req = requests.get(link, headers=headers)
        new_transaction = req.json()
        for i in range(min(len(old_transactions), len(new_transaction))):
            if new_transaction[i] in old_transactions:
                continue
            else:
                if new_transaction[i].get("method") == "buy" and int(
                        new_transaction[i].get('transactionPriceUSD')) >= 50:
                    new_buy = new_transaction[i]
                    update.message.reply_text(
                        f"""Rug Muncher BOT found a big buy on FEGex of LOT\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n For total of {new_buy.get('transactionPriceUSD')}$""")


def getpricesrug(tipe):
    if tipe == "rmt" :
        link = "https://fegex-v2-api.fegex.com/additional-data?id=RUGMUNCHERTOKENfBNB-bsc-dc"
    else :
        link = "https://fegex-v2-api.fegex.com/additional-data?id=LOTTERYfBNB-bsc-bf"
    req = requests.get(link, headers=headers)
    return req.json()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_text(f'Hi! price is {format(getpricesrug().get("tokenPriceUSD"), ".12f")}')


def function(update,tipe):
    js = getpricesrug(tipe)
    if tipe == "rmt":
        while True:
            if js.get("tokenPriceUSD") != main.price_rmt:
                string = f""" * [Price] {js.get("name")} *  ```  \nPrice USD: ${format(main.price_rmt, ".12f")} -> ${format(js.get("tokenPriceUSD"), ".12f")}\nPrice BNB: {format(main.prix_bnb_rmt, ".16f")} -> {format(js.get("tokenPrice"), ".16f")}\nPrice change: {format(js.get("priceChangePercentage"), ".4f")}% \n \nMarketcap: ${int(js.get("marketCap")) / 1000}k\nVolume 24h: ${round(float(js.get("volume24hData").get("buy")), 4) + round(float(js.get("volume24hData").get("sell")), 4)}k\nBuy: ${round(float(js.get("volume24hData").get("buy")), 4)} / Sell: ${round(float(js.get("volume24hData").get("sell")), 4)}\nTransactions: {int(js.get("count24hData").get("buy")) + int(js.get("count24hData").get("sell"))}\n ```
                                                 """
                update.message.reply_text(string, parse_mode="Markdown")
                main.prix_bnb_rmt = js.get("tokenPrice")
                main.price_rmt = js.get("tokenPriceUSD")
                time.sleep(30)
    else :
        while True:
            if js.get("tokenPriceUSD") != main.price_lot:
                string = f""" * [Price] {js.get("name")} *  ```  \nPrice USD: ${format(main.price_lot, ".12f")} -> ${format(js.get("tokenPriceUSD"), ".12f")}\nPrice BNB: {format(main.prix_bnb_lot, ".16f")} -> {format(js.get("tokenPrice"), ".16f")}\nPrice change: {format(js.get("priceChangePercentage"), ".4f")}% \n \nMarketcap: ${int(js.get("marketCap")) / 1000}k\nVolume 24h: ${round(float(js.get("volume24hData").get("buy")), 4) + round(float(js.get("volume24hData").get("sell")), 4)}k\nBuy: ${round(float(js.get("volume24hData").get("buy")), 4)} / Sell: ${round(float(js.get("volume24hData").get("sell")), 4)}\nTransactions: {int(js.get("count24hData").get("buy")) + int(js.get("count24hData").get("sell"))}\n ```                                   """
                update.message.reply_text(string, parse_mode="Markdown")
                main.prix_bnb_lot = js.get("tokenPrice")
                main.price_lot = js.get("tokenPriceUSD")
                time.sleep(30)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main(token):
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


def echo(update, context):
    message = update.message.text
    if message == "track_price" or message == "track_transaction" or message == "track_buy_transaction" :
        update.message.reply_text("""* Please enter the name of the token that you want to track (rmt/lot)*""", parse_mode="Markdown")
        return
    elif "track_transaction lot" in message and main.s_ == "test":
        t = Thread(target=get_transaction, args=(update,"lot",))
        t.start()
        main.s_ = "t"
        return
    elif "track_buy_transaction lot" in message and main.st_ == "test":
        t = Thread(target=get_buy_transaction, args=(update,"lot",))
        t.start()
        main.st_ = "t"
        return
    elif "track_price lot" in message and main.state_ == "test":
        main.price_lot = getpricesrug("lot").get("tokenPriceUSD")
        main.prix_bnb_lot = getpricesrug("lot").get("tokenPrice")
        new_thread = Thread(target=function, args=(update, "lot",))
        new_thread.start()
        main.state_ = "t"
        js = getpricesrug("lot")
        string = f""" * [Price] {js.get("name")} *  ```  \nPrice USD: ${format(main.price_lot, ".12f")} \nPrice BNB: {format(main.prix_bnb_lot, ".16f")} \nPrice BNB: {format(js.get("tokenPrice"), ".16f")}\nPrice change: {format(js.get("priceChangePercentage"), ".4f")}% \n \nMarketcap: ${int(js.get("marketCap")) / 1000}k\nVolume 24h: ${round(float(js.get("volume24hData").get("buy")), 4) + round(float(js.get("volume24hData").get("sell")), 4)}k\nBuy: ${round(float(js.get("volume24hData").get("buy")), 4)} / Sell: ${round(float(js.get("volume24hData").get("sell")), 4)}\nTransactions: {int(js.get("count24hData").get("buy")) + int(js.get("count24hData").get("sell"))}\n ```"""
        update.message.reply_text(string, parse_mode="Markdown")
        return
    elif "track_transaction rmt" in message and main.s == "test":
        t = Thread(target=get_transaction, args=(update,"rmt",))
        t.start()
        main.s = "t"
        return
    elif "track_buy_transaction rmt" in message and main.st == "test":
        t = Thread(target=get_buy_transaction, args=(update,"rmt",))
        t.start()
        main.st = "t"
        return
    elif  "track_price rmt" in message and main.state == "test":
        main.price_rmt = getpricesrug("rmt").get("tokenPriceUSD")
        main.prix_bnb_rmt = getpricesrug("rmt").get("tokenPrice")
        new_thread = Thread(target=function, args=(update,"rmt",))
        new_thread.start()
        main.state = "t"
        js = getpricesrug("rmt")
        string = f""" * [Price] {js.get("name")} *  ```  \nPrice USD: ${format(main.price_rmt, ".12f")} \nPrice BNB: {format(main.prix_bnb_rmt, ".16f")} \nPrice BNB: {format(js.get("tokenPrice"), ".16f")}\nPrice change: {format(js.get("priceChangePercentage"), ".4f")}% \n \nMarketcap: ${int(js.get("marketCap")) / 1000}k\nVolume 24h: ${round(float(js.get("volume24hData").get("buy")), 4) + round(float(js.get("volume24hData").get("sell")), 4)}k\nBuy: ${round(float(js.get("volume24hData").get("buy")), 4)} / Sell: ${round(float(js.get("volume24hData").get("sell")), 4)}\nTransactions: {int(js.get("count24hData").get("buy")) + int(js.get("count24hData").get("sell"))}\n ```"""
        update.message.reply_text(string, parse_mode="Markdown")
        return
    elif ("track_price rmt" in message and main.state != "test") or (
            "track_buy_transaction rmt" in update.message.text  and main.st != "test") or (
           "track_transaction rmt" in message and main.s != "test") or ("track_price lot" in message and main.state_ != "test") or (
           "track_buy_transaction lot" in message and main.st_ != "test") or (
            "track_transaction lot" in message and main.s_ != "test"):
        update.message.reply_text("""*Rug Muncher BOT  IS ALREADY TRACKING TOKENS*""", parse_mode="Markdown")
        return


if __name__ == '__main__':
    main.state = "test"
    main.st = "test"
    main.s = "test"
    main.state_ = "test"
    main.st_ = "test"
    main.s_ = "test"
    token = input('Please enter your telegram bot token : ')
    main(token)
