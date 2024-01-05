import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from details.handlers import (
    start,
    add_movie,
    menu,
    movie,
    qidiruv,
    text,
    stats,
    button_callback
)
TOKEN = "6667437345:AAEuOd2azkUKvwlat_4Uxy5L7bLoLtasnuk"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def register_handlers():

    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(MessageHandler(Filters.text("Добавить фильм➕"),add_movie)),
    dispatcher.add_handler(MessageHandler(Filters.text("Назад⬅️"), menu)),
    dispatcher.add_handler(MessageHandler(Filters.text("Поиск🔍"), qidiruv)),
    dispatcher.add_handler(MessageHandler(Filters.video, movie)),
    dispatcher.add_handler(MessageHandler(Filters.text('Статистика📊'), stats)),
    dispatcher.add_handler(MessageHandler(Filters.text, text)),
    dispatcher.add_handler(CallbackQueryHandler(button_callback)),


    

    updater.start_polling()
    updater.idle()


register_handlers()