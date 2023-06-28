from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_menu import d_key

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name},\n IT Center Bulungur  botga xush kelibsiz!",reply_markup=d_key)
