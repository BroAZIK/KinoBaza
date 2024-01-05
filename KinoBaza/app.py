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

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():

    if request.method == "GET":
        return "Hello from webhook!"

    if request.method == "POST":

        print("Post keldi!")
        body = request.get_json()
        update = Update.de_json(body, bot)

        dispatcher.add_handler(CommandHandler("start", start)),
        dispatcher.add_handler(MessageHandler(Filters.text("Добавить фильм➕"),add_movie)),
        dispatcher.add_handler(MessageHandler(Filters.text("Назад⬅️"), menu)),
        dispatcher.add_handler(MessageHandler(Filters.text("Поиск🔍"), qidiruv)),
        dispatcher.add_handler(MessageHandler(Filters.video, movie)),
        dispatcher.add_handler(MessageHandler(Filters.text('Статистика📊'), stats)),
        dispatcher.add_handler(MessageHandler(Filters.text, text)),
        dispatcher.add_handler(CallbackQueryHandler(button_callback)),

        dispatcher.process_update(update)

        return {"message":"ok"}



if __name__ == "__main__":
    app.run(debug=True)