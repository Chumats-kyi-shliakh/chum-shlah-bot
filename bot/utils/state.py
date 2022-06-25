from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuStates(StatesGroup):
    menu = State()


class AddStorageStates(StatesGroup):
    add_storage = State()
    input_name = State()
    input_gis = State()


class AddProductStates(StatesGroup):
    choose_category = State()
    input_name = State()
    input_weight = State()
    input_shape = State()


