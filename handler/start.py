from aiogram import Router, F
from aiogram.types import Message,CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from datetime import datetime

from states import Task

from keyboards import START_BUTTON, TAVSIF_BUTTON

start_r = Router()

@start_r.message(CommandStart())
async def start(message:Message):
    await message.answer("Botga xush kelibsiz",reply_markup=START_BUTTON)


@start_r.message(F.text == "Add task")
async def barcha(message:Message, state:FSMContext):
    await message.answer("📝 Yangi vazifa nomini kiriting:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Task.title)

@start_r.message(Task.title)
async def get_title(message:Message, state:FSMContext):
    title = message.text
    if title:
        await message.answer("Qo‘shimcha ma’lumot kiriting (ixtiyoriy):", reply_markup=TAVSIF_BUTTON)
        await state.update_data(title = title)
        await state.set_state(Task.description)
    else:
        await message.answer("Sarlavhani bo'sh qoldirmang")
    await message.answer(title)

@start_r.message(Task.description)
async def get_tavsif(message:Message, state:FSMContext):
    tavsif = message.text
    if tavsif == "Shart emas":
        await state.update_data(description = "Malumot yo'q")
    else:
        await state.update_data(description = tavsif)
    await message.answer("Tugash sanasini yozing (YYYY-MM-DD HH:MM) formatda, \nMasalan: 2025-10-27 23:59")
    await state.set_state(Task.deadline)
    await message.answer(tavsif)

@start_r.message(Task.deadline)
async def get_muddat(message:Message, state:FSMContext):
    muddat = message.text
    await message.answer(muddat)
    try:
        sana = datetime.strptime(muddat,"%Y-%m-%d %H:%M")
    except:
        await message.answer("Vaqtni to'g'ri (YYYY-MM-DD HH:MM) formatda yozing:")

    now = datetime.now()
    if sana > now:
        await state.update_data(deadline = muddat)
        await message.answer("Malumot saqlandi qilindi")
        await state.clear()
    else:
        await message.answer("muddat o'tib ketgan")


    



