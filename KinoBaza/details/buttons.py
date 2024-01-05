from telegram import InlineKeyboardButton
all_start = [
    ["Поиск🔍"],
    ["Статистика📊","Админ👨🏻‍💻"]
]
adm_start = [
    ["Добавить фильм➕"],
    ["Статистика📊"]
]

back = [
    ["Назад⬅️"]
]

inline_keyboard = [
        [InlineKeyboardButton("Подписаться❌", url="https://t.me/Tarjima_Kinolar_Celestial")],
        [InlineKeyboardButton("Проверка✅", callback_data='subscribe')]
    ]