from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.parsemode import ParseMode
from database.db import get, update_db, insert, delete, soni
from .buttons import *
from pprint import pprint
import json

Admin_id = 5027127747
channel_id = 2008534772
channel = "@Tarjima_Kinolar_Celestial"

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    counts = soni()
    users_count = counts['users']
    movies_count = counts['movies']

    if user_id == Admin_id:
        update.message.reply_text(
            text=f"🤖Количество пользователей бота: {users_count}👤\n\n🎥Количество фильмов: {movies_count}📹",
            reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )
        try:
            insert(table="stage",user_id=user_id, data={'stage': "start"})
        except:
            pass
    else:
        is_subscribed = context.bot.get_chat_member(channel, user_id).status == 'member'
        if is_subscribed == True:
            user = {'stage': "start"}
            try:
                insert(table="stage",user_id=user_id, data=user)
                insert(table="users",user_id=user_id, data={"first_name":update.effective_chat.first_name,"last_name": update.effective_chat.last_name})

                try:
                    update.message.reply_html(
                    text="Здравствуйте и добро пожаловать в наш бот!😊",
    
                    )
                    update.message.reply_text(
                    text="Выберите один из разделов ниже👇",
                    reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
                    )
                except:
                    pass

            except:
                update_db(table="stage", user_id=user_id,data=user)

                update.message.reply_text(
                    text="Выберите один из разделов ниже👇",
                    reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
                    )
        else:
            update.message.reply_text(
                text="Подпишитесь на наш канал!",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
            )   
def add_movie(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update_db(table="stage", user_id=user_id,data={"stage":"add_movie"})

    update.message.reply_text(
        text="Отправить фильм...",
        reply_markup=ReplyKeyboardMarkup(back, resize_keyboard=True)
    )

def menu(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update_db(table="stage", user_id=user_id,data={"stage":"start"})
    
    
    counts = soni()
    users_count = counts['users']
    movies_count = counts['movies']
        

    if user_id == Admin_id:
        update.message.reply_text(
            text=f"🤖Количество пользователей бота: {users_count}👤\n\n🎥Количество фильмов: {movies_count}📹",
            reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )
    else:
        update.message.reply_text(
            text="Выберите один из разделов ниже👇",
            reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
            )

def movie(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update_db(table="stage", user_id=user_id,data={"stage":"uploading"})

    update_json = json.dumps(update.to_dict(), indent=2, ensure_ascii=False)
    pprint(json.loads(update_json))
    stage = get(table="stage", user_id=user_id)
    stage = stage['stage']

    if user_id == Admin_id:
        if stage == "add_movie" or "uploading":

  
            file_id = update.message.video.file_id
            file_name = update.message.video.file_name
            file_type = update.message.video.mime_type

            file_thumb = update.message.video.thumb.file_id

            doc_id = insert(table="movies",data={'file_id': file_id,"file_name": file_name, "file_type": file_type, "file_thumb": file_thumb}, user_id=user_id)
            update.message.reply_video(video=file_id,
                                    caption = f"Фильм успешно сохранен. ✅\n\nКод фильма: {doc_id}💎\nНазвание фильма: {file_name}🎩\nТип фильма: {file_type}📽", 
                                    reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True))

            update_db(table="stage", user_id=user_id,data={"stage":"start"})
        else:
            update.message.reply_text(text="Неправильный ход!", reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True))
            update_db(table="stage", user_id=user_id,data={"stage":"start"})
    else:
        update.message.reply_text(
            text="Вы не админ!",
            reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
        )
def qidiruv(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update_db(table="stage", user_id=user_id,data={"stage":"qidiruv"})
    update.message.reply_text(
        text="Введите код фильма, который вы хотите найти..",
        reply_markup=ReplyKeyboardMarkup(back, resize_keyboard=True)
    )

def text(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    stage = get(table="stage", user_id=user_id)
    print(stage)

    if stage['stage'] == "qidiruv":
        try:
            kino = get(table="movies", user_id=update.message.text)
            pprint(kino)
            update.message.reply_video(
                video=kino['file_id'],
                reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
            )
            update_db(table="stage", user_id=user_id,data={"stage":"start"})
        
        except:
            update.message.reply_text(
                text="Фильм не найден!",
                reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
            )
            update_db(table="stage", user_id=user_id,data={"stage":"start"})
    elif update.message.text == "Админ👨🏻‍💻":
        update.message.reply_text(
            text="Админ: @Aziz_Khujamov👨🏻‍💻\n(это сообщение изменится в соответствии с вашими требованиями!)",
            reply_markup=ReplyKeyboardMarkup(back, resize_keyboard=True)
        )


def stats(update: Update, context: CallbackContext):
    counts = soni()
    users_count = counts['users']
    movies_count = counts['movies']

    if Admin_id == update.effective_chat.id:

        update.message.reply_text(
        text=f"Количество пользователей: {users_count}👤\n\nКоличество фильмов: {movies_count}📹",
        reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )
    else:
        update.message.reply_text(
        text=f"Количество пользователей: {users_count}👤\n\nКоличество фильмов: {movies_count}📹",
        reply_markup=ReplyKeyboardMarkup(back, resize_keyboard=True)
        )

def button_callback(update, context):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'subscribe':
        # Obuna bo'ldim tugmasi bosilganda
        query.answer("Вы подписались на канал!")
        context.bot.send_message(chat_id=user_id, text="Выберите один из разделов ниже👇🏻",reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True))



    else:
        query.answer("Вы не подписаны на канал!❌")
    