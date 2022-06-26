from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.utils.constants import MENU_BTN


class MainKeyboard:

    @staticmethod
    def menu_keyboard_btn():
        menu = KeyboardButton(MENU_BTN)
        return ReplyKeyboardMarkup().add(menu)

    @staticmethod
    def menu_inline_btn():
        result_kb = InlineKeyboardMarkup(row_width=1)
        add_storage = InlineKeyboardButton('➕ Додати склад', callback_data='add_storage')
        add_product = InlineKeyboardButton('➕ Додати товар', callback_data='add_product')
        edit_stock = InlineKeyboardButton('📝 Оновити наявність', callback_data='edit_stock')
        order_items = InlineKeyboardButton('➕ Додати замовлення', callback_data='order_items')
        close = InlineKeyboardButton('❌ Закрити', callback_data='close')
        return result_kb.add(add_storage, edit_stock, add_product, order_items, close)

    @staticmethod
    def input_gis():
        result_kb = ReplyKeyboardMarkup(row_width=1)
        gis = KeyboardButton('🗺 Відправити локацію', request_location=True)
        return result_kb.add(gis)

    @staticmethod
    def save_cancel():
        result_kb = InlineKeyboardMarkup(row_width=2)
        save = InlineKeyboardButton('✅ Зберегти', callback_data='save')
        cancel = InlineKeyboardButton('❌ Відмінити', callback_data='cancel')
        return result_kb.add(save, cancel)

    @staticmethod
    def categories(categories):
        result_kb = InlineKeyboardMarkup(row_width=1)
        for category in categories:
            c_btn = InlineKeyboardButton(f'{category.get("name")}', callback_data=f'category_{category.get("id")}')
            result_kb.add(c_btn)
        return result_kb