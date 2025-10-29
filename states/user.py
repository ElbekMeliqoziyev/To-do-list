from aiogram.fsm.state import State, StatesGroup

class Task(StatesGroup):
    title = State()
    description = State()
    deadline = State()