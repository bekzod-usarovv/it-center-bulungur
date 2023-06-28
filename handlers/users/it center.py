from aiogram import types
from loader import dp

@dp.message_handler(text="🏢 IT Center Bulung'ur haqida malumot")
async def courses_fun(message: types.Message):
    await message.answer("Kurslarimiz haqida malumot",
                         "IT Center Bulung'ur 06.06.2020 yildan ochilgan "
                         "va hozirda 1.web dasturlash 2.mobil dasturlash 3.Grafik dizayn 4.Kompyuter savotxinligi "
                         "yo'lalishlarida o'quvchilatga ta'lim berib kelmoqda")