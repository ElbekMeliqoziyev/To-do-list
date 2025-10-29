from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

START_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="My task"), KeyboardButton(text="Add task")],
        [KeyboardButton(text="Delete task"), KeyboardButton(text="Edit task")]   
    ],
    resize_keyboard=True
)

TAVSIF_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Shart emas")]
    ],
    resize_keyboard=True
)