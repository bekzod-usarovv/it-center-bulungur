from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


d_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 IT Center haqida malumot")
        ],
        [
            KeyboardButton(text="📚 Kurslar haqida"),
            KeyboardButton(text="📝 Murojatlar"),

        ],
    ],
    resize_keyboard=True
)