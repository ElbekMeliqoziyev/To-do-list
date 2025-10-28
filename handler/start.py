from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart

from keyboards import START_BUTTON

start_r = Router()

@start_r.message(CommandStart())
async def start(message:Message):
    await message.answer("Botga xush kelibsiz",reply_markup=START_BUTTON)


@start_r.message(F.text == "Add task")
async def barcha(message:Message):
    pass



# @start_r.message()
# async def echo(message:Message):
#     await message.answer(message.text)