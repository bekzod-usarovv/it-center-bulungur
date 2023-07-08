from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_menu import d_key

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name},\n IT Center Bulungur  botga xush kelibsiz!",reply_markup=d_key)


# @dp.message_handler(text="🏢 IT Center Bulung'ur haqida malumot")
# async def courses_fun(message: types.Message):
#     await message.answer("Kurslarimiz haqida malumot",
#                          "IT Center Bulung'ur 06.06.2020 yildan ochilgan "
#                          "va hozirda 1.web dasturlash 2.mobil dasturlash 3.Grafik dizayn 4.Kompyuter savotxinligi "
#                          "yo'lalishlarida o'quvchilatga ta'lim berib kelmoqda")