from aiogram.dispatcher.filters.state import State

from aiogram.dispatcher.filters.state import StatesGroup


class ClientRequest(StatesGroup):
    additional = State()
