from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


d_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 IT Center Bulung'ur haqida malumot")
        ],
        [
            KeyboardButton(text="📚 Kurslar haqida"),
            KeyboardButton(text="📝 Ro'yxatdan o'tish"),
            KeyboardButton(text="📋 Murojatlar"),
        ],
        [
            KeyboardButton(text="🗺 Manzil"),
            KeyboardButton(text="📞 Bog'laish"),
        ],

    ],
    resize_keyboard=True
)