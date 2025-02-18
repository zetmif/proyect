# from aiogram.dispatcher import FSMContext
# from states.anketastate import AnketaState
# from aiogram import types
# from loader import dp,bot
#
# @dp.message_handler(commands="anketa")
# async def anketa_function(message:types.Message):
#     await message.answer("Sizga bir nechta savollar beramiz")
#     await message.answer("Ismingizni kiriting")
#     await AnketaState.ism.set()
#
# @dp.message_handler(state=AnketaState.ism)
# async def ism_holati(message:types.Message,state:FSMContext):
#     ism=message.text
#     await state.update_data(
#         {"ism":ism}
#     )
#     await message.answer("Familiyangizni kiriting:")
#     await AnketaState.familiya.set()
# @dp.message_handler(state=AnketaState.familiya)
# async def familiya_holati(message:types.Message,state:FSMContext):
#     familiya=message.text
#     await state.update_data(
#         {"familiya":familiya}
#     )
#
#     #malumotlarni oqiymiz
#     data=await state.get_data()
#     ism=data.get("ism")
#     familiya=data.get("familiya")
#
#     text=f"Quyidagi ma'lumotlar oling\n"
#     text+=f"ism:{ism}\n"
#     text+=f"familiya:{familiya}\n"
#     text+=f"username:@{message.from_user.username}"
#     await message.answer(text)

