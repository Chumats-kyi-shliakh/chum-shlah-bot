from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.utils.keyboard import MainKeyboard
from bot.utils.messages import MESSAGES
from bot.utils.state import AddStorageStates, MenuStates


async def callback_add_storage(callback_query: types.CallbackQuery, state: FSMContext):
    await AddStorageStates.add_storage.set()
    await callback_query.message.edit_text(MESSAGES['add_storage']['input_name'])


async def message_input_storage_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['input_name'] = message.text
    await AddStorageStates.input_name.set()
    await message.reply(MESSAGES['add_storage']['input_gis'])


async def message_input_storage_gis(message: types.Message, state: FSMContext):
    await AddStorageStates.input_gis.set()
    async with state.proxy() as data:
        data['latitude'] = message.location.latitude
        data['longitude'] = message.location.longitude
    await message.reply(MESSAGES['add_storage']['save_cancel'], reply_markup=MainKeyboard.save_cancel())


async def callback_save_cancel_storage(callback_query: types.CallbackQuery, state: FSMContext):
    await MenuStates.menu.set()

    if callback_query.data == 'cancel':
        await callback_query.message.edit_text(MESSAGES['add_storage']['cancel'] + MESSAGES['menu']['menu'],
                                               reply_markup=MainKeyboard.menu_inline_btn())
        return

    async with state.proxy() as data:
        latitude = data['latitude']
        longitude = data['longitude']
        input_name = data['input_name']

    # post in db

    await callback_query.message.edit_text(MESSAGES['add_storage']['save'] + MESSAGES['menu']['menu'],
                                           reply_markup=MainKeyboard.menu_inline_btn())
