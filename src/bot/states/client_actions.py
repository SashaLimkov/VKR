from aiogram.dispatcher.filters.state import State

from aiogram.dispatcher.filters.state import StatesGroup


class ClientRequest(StatesGroup):
    additional = State()
    waiting_for_answer = State()

class RegWorker(StatesGroup):
    editing = State()