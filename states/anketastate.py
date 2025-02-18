from aiogram.dispatcher.filters.state import StatesGroup,State



class AnketaState(StatesGroup):
    familiya_ism=State()
    telefonraqam=State()
    yosh=State()
    manzil=State()
    kurslar=State()
    narx=State()
    kasbi=State()
    murojat=State()
    maqsad=State()