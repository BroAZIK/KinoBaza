from telegram import Bot
TOKEN = "6667437345:AAEuOd2azkUKvwlat_4Uxy5L7bLoLtasnuk"

bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    url = 'https://azizbek2007.pythonanywhere.com/webhook'
    print(bot.set_webhook(url=url))

set()