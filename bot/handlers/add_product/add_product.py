from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.utils.keyboard import MainKeyboard
from bot.utils.messages import MESSAGES
from bot.utils.state import MenuStates


async def callback_add_product(callback_query: types.CallbackQuery, state: FSMContext):

