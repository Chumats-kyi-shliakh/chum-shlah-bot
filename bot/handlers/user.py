from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from bot.handlers.add_product.add_product import callback_add_product
from bot.handlers.add_storage.add_storage import callback_add_storage, message_input_storage_name, \
    message_input_storage_gis, callback_save_cancel_storage
from bot.utils.constants import MENU_BTN
from bot.utils.keyboard import MainKeyboard
from bot.utils.messages import MESSAGES
from bot.utils.state import MenuStates, AddStorageStates


async def command_start_login_handler(message: types.Message, state: FSMContext):
    await message.answer(MESSAGES['menu']['start'].format(user=message.from_user.username),
                         reply_markup=MainKeyboard.menu_keyboard_btn())


async def close_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text(MESSAGES['menu']['close'])


async def menu_handler(message: types.Message, state: FSMContext):
    await MenuStates.menu.set()
    await message.answer(MESSAGES['menu']['menu'], reply_markup=MainKeyboard.menu_inline_btn())


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start_login_handler, state='*', commands=['start'])
    dp.register_callback_query_handler(close_handler, lambda c: c.data == 'close', state='*')
    dp.register_message_handler(menu_handler, lambda m: m.text == MENU_BTN, state='*')

    # add storage states
    dp.register_callback_query_handler(callback_add_storage, lambda c: c.data == 'add_storage',
                                       state=MenuStates.menu)
    dp.register_message_handler(message_input_storage_name, state=AddStorageStates.add_storage)
    dp.register_message_handler(message_input_storage_gis, state=AddStorageStates.input_name,
                                content_types=['location'])
    dp.register_callback_query_handler(callback_save_cancel_storage, lambda c: c.data in ['save', 'cancel'],
                                       state=AddStorageStates.input_gis)

    # add_product
    dp.register_callback_query_handler(callback_add_product, lambda c: c.data == 'add_product',
                                       state=MenuStates.menu)
    dp.register_callback_query_handler()
    # edit_stock

    # order_items
