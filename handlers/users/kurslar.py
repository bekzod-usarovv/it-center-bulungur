from aiogram import types
from loader import dp
from keyboards.inline.inline_kurs import kurs

@dp.message_handler(text='📚 Kurslar haqida')
async def courses_fun(message: types.Message):
    await message.answer("Kurslarimiz haqida malumot",reply_markup=kurs)