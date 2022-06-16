from aiogram import types
from aiogram.dispatcher import FSMContext


async def skip_test(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data.get("cd"))