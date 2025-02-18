from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Barcha kinolar"),
            KeyboardButton(text="kino qidirish")

        ],
        [
            KeyboardButton(text="Dasturchi"),
            KeyboardButton(text="admin")
        ],
        [
            KeyboardButton(text="Kanalga obuna")
        ]
    ],
    resize_keyboard=True
)