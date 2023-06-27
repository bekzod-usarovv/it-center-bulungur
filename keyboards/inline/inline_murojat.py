from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

murojat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="IT Markaz Menejoriga murojat", callback_data='web_d')
        ],
        [
            InlineKeyboardButton(text="Frontend o'qitivchiga murojat", callback_data='mobile_d'),
            InlineKeyboardButton(text="Kompyuter savodxonligi", callback_data='mobile_d')

        ],
    ],
)






