from aiogram.dispatcher import FSMContext
from states.anketastate import AnketaState
from aiogram import types
from loader import dp,bot
from data.config import ADMINS



@dp.message_handler(commands="ariza")
async def anketa_function(message:types.Message):
    await message.answer("Ish joyi topish uchun ariza berish "
                         "Hozir sizga birnecha savollar beriladi. "
                         "Har biriga javob bering. "
                         "Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi")
    await message.answer("Ism, familiyangizni kiriting?")
    await AnketaState.familiya_ism.set()

@dp.message_handler(state=AnketaState.familiya_ism)
async def familiyaism_holati(message:types.Message,state:FSMContext):
    familiya_ism=message.text
    await state.update_data(
        {"familiya_ism":familiya_ism}
    )
    await message.answer("📞 Aloqa: Bog`lanish uchun raqamingizni kiriting?"
                         "Masalan, +998 90 123 45 67")
    await AnketaState.telefonraqam.set()
@dp.message_handler(state=AnketaState.telefonraqam)
async def telefonraqam_holati(message: types.Message, state: FSMContext):
    telefonraqam= message.text
    await state.update_data(
        {"telefonraqam":telefonraqam }
           )
    await message.answer("🕑Yosh: "
                         "Yoshingizni kiriting?"
                         "Masalan, 19")
    await AnketaState.yosh.set()
@dp.message_handler(state=AnketaState.yosh)
async def yosh_holati(message: types.Message, state: FSMContext):
    yosh= message.text
    await state.update_data(
        {"yosh": yosh}
    )
    await message.answer("🌐 Hudud:Qaysi hududdansiz?"
                         "Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await AnketaState.manzil.set()
@dp.message_handler(state=AnketaState.manzil)
async def manzil_holati(message: types.Message, state: FSMContext):
    manzil= message.text
    await state.update_data(
        {"manzil":manzil }
           )
    await message.answer("📚 Texnologiya:"
                         "Talab qilinadigan texnologiyalarni kiriting?"
                         "Texnologiya nomlarini vergul bilan ajrating. Masalan, Java, C++, C#")
    await AnketaState.kurslar.set()
@dp.message_handler(state=AnketaState.kurslar)
async def kurslar_holati(message: types.Message, state: FSMContext):
    kurs= message.text
    await state.update_data(
        {"Kurslar":kurs }
           )



    await message.answer("💰 Narxi:Tolov qilasizmi yoki Tekinmi?"
                         "Kerak bo`lsa, Summani kiriting?")

    await AnketaState.narx.set()
@dp.message_handler(state=AnketaState.narx)
async def narx_holati(message:types.Message,state:FSMContext):
    narx=message.text
    await state.update_data(
        {"narx": narx }
    )

    await message.answer("👨🏻‍💻 Kasbi: Ishlaysizmi yoki o`qiysizmi? Masalan, Talaba")
    await AnketaState.kasbi.set()
@dp.message_handler(state=AnketaState.kasbi)
async def kasbi_holati(message:types.Message,state:FSMContext):
    kasbi=message.text
    await state.update_data(
        {"kasbi":kasbi}
    )

    await message.answer("🕰 Murojaat qilish vaqti: Qaysi vaqtda murojaat qilish mumkin? Masalan, 9:00 - 18:00")
    await AnketaState.murojat.set()
@dp.message_handler(state=AnketaState.murojat)
async def murojat_holati(message:types.Message,state:FSMContext):
    murojat=message.text
    await state.update_data(
        {"murojat":murojat}
    )

    await message.answer("🔎 Maqsad: Maqsadingizni qisqacha yozib bering")
    await AnketaState.maqsad.set()
@dp.message_handler(state=AnketaState.maqsad)
async def maqsad_holati(message:types.Message,state:FSMContext):
    maqsad=message.text
    await state.update_data(
        {"maqsad":maqsad}
    )




    # malumotlarni oqiymiz
    data = await state.get_data()
    ism_familiya = data.get("familiya_ism")
    telefonraqam= data.get("telefonraqam")
    yosh=data.get("yosh")
    manzil=data.get("manzil")
    kurslar=data.get("kurslar")
    narx=data.get("narx")
    kasbi=data.get("kasbi")
    murojat=data.get("murojat")
    maqsad=data.get(("maqsad"))

    text = f"Quyidagi ma'lumotlar oling\n"
    text += f"familiya_ism:{ism_familiya}\n"
    text += f"telefonraqam:{telefonraqam}\n"
    text +=f"yosh:{yosh}\n"
    text+=f"hudud:{manzil}\n"
    text+=f"texnologiya:{kurslar}\n"
    text+=f"narx:{narx}\n"
    text+=f"kasbi:{kasbi}\n"
    text+=f"murojat vaqti;{murojat}\n"
    text+=f"maqsad:{maqsad}"
    text += f"username:@{message.from_user.username}\n"
    await message.answer(text)