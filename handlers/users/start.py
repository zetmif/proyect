from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu_start
from loader import dp,bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomu aleykum xush kelibsiz",reply_markup=menu_start)
    username=message.from_user.username
    full_name=message.from_user.full_name
    tg_id=message.from_user.id
    text=f"Botda yangi foydalanuvchi qo'shildi\n"
    text+=f"username:{username}\n"
    text+=f"full_name:{full_name}\n"
    text+=f"tg_id:{tg_id}\n"
    for admin in ADMINS:
        await bot.send_message(chat_id=admin,text=text)

# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def photo_handler(message:types.Message):
#     photo = message.photo[-1].file_id
#     # await message.reply("Bu qanday rasm ?")
#     for admin in ADMINS:
#         await bot.send_photo(chat_id=admin,photo=photo)





