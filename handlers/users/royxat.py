from aiogram import types
from loader import dp,bot
from states.royxatga_olish import MurojatState
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="📝 Ro'yxatdan o'tish")
async def drektor_murojat(message: types.Message):
    await message.answer("Assalomu alaykum!!! \n Drektorga murojat qilish uchun bazi bir malumotlar talab qilinadi")
    await message.answer('Agarda rozi bo\'salgiz Ism Familiyagizni yuboring')
    await MurojatState.fish.set()




@dp.message_handler(state=MurojatState.fish)
async def ismfam(message: types.Message, state: FSMContext):
    ism_fam = message.text
    await state.update_data(
        {'full_name': ism_fam}
    )
    await message.answer('Endi telefon raqamingizni yuboring')
    await MurojatState.next()




@dp.message_handler(state=MurojatState.phone)
async def phonefun(message: types.Message, state: FSMContext):
    tel = message.text
    await state.update_data(
        {'phone': tel}
    )
    await message.answer('Endi manzil yuboring')
    await MurojatState.next()



@dp.message_handler(state=MurojatState.manzil)
async def manzil(message: types.Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {'address': manzil}
    )
    await message.answer('Endi murojat yuboring')
    await MurojatState.next()



@dp.message_handler(state=MurojatState.text)
async def murojat(message: types.Message, state: FSMContext):
    murojat_text = message.text
    await state.update_data(
        {'text': murojat_text}
    )

    full_info = await state.get_data()
    full_name = full_info.get('full_name')
    phone = full_info.get('phone')
    manzil = full_info('address')
    text = full_info.get('text')
    sent_info = f"{full_name}\n{phone}\n{manzil}\n{text}"
    await bot.send_message(chat_id=1445384329, text=sent_info)


    await state.finish()

