import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.utils.keyboard import MainKeyboard
from bot.utils.messages import MESSAGES
from bot.utils.state import MenuStates, AddProductStates


async def callback_add_product(callback_query: types.CallbackQuery, state: FSMContext):
    await AddProductStates.choose_category.set()
    categories = requests.get(url='https://chum-shlakh-rails-test.herokuapp.com/api/v1/categories')
    categories_json = categories.json()
    await callback_query.message.edit_text(MESSAGES['add_product']['select_category'],
                                           reply_markup=MainKeyboard.categories(categories_json))


async def callback_select_category(callback_query: types.CallbackQuery, state: FSMContext):
    await AddProductStates.input_name.set()
    async with state.proxy() as data:
        data['category_id'] = callback_query.data.split('_')[1]
    await callback_query.message.edit_text(MESSAGES['add_product']['input_name'])


async def input_name_handler(message: types.Message, state: FSMContext):
    await AddProductStates.input_weight.set()
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply(MESSAGES['add_product']['input_weight'])


async def input_weight_handler(message: types.Message, state: FSMContext):
    await AddProductStates.input_shape.set()
    async with state.proxy() as data:
        data['weight'] = message.text
    await message.reply(MESSAGES['add_product']['input_shape'])


async def input_shape_handler(message: types.Message, state: FSMContext):
    shape = message.text.split()
    await AddProductStates.save_cancel.set()
    async with state.proxy() as data:
        data['shape'] = shape
    await message.reply(MESSAGES['add_product']['save_cancel'], reply_markup=MainKeyboard.save_cancel())


async def callback_save_cancel_product(callback_query: types.CallbackQuery, state):
    await MenuStates.menu.set()

    if callback_query.data == 'cancel':
        await callback_query.message.edit_text(MESSAGES['add_product']['cancel'] + MESSAGES['menu']['menu'],
                                               reply_markup=MainKeyboard.menu_inline_btn())
        return

    async with state.proxy() as data:
        shape = data['shape']
        category_id = data['category_id']
        name = data['name']
        weight = data['weight']

    # post in db

    await callback_query.message.edit_text(MESSAGES['add_product']['save'] + MESSAGES['menu']['menu'],
                                           reply_markup=MainKeyboard.menu_inline_btn())
