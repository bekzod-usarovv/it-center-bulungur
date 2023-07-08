from aiogram import types
from loader import dp


@dp.message_handler(text="🏢 IT Center Bulung'ur haqida malumot")
async def courses_fun(message: types.Message):
    await message.answer("🏢 IT Center Bulung'ur haqida malumot"
                         "IT Center Bulung'ur 06.06.2020 yildan ochilgan va hozirda \n1.web dasturlash \n2.mobil dasturlash \n3.Grafik dizayn \n4.Kompyuter savotxinligi \n yo'lalishlarida o'quvchilatga ta'lim berib kelmoqda")


@dp.message_handler(text="📞 Bog'laish")
async def courses_fun(message: types.Message):
    await message.answer("📞 Bog'laish"
                         "Telefon raqam +998 97 915 92 92")