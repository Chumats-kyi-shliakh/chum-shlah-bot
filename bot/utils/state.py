from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuStates(StatesGroup):
    menu = State()


class AddStorageStates(StatesGroup):
    input_name = State()
    input_gis = State()
    save_cancel = State()


class AddProductStates(StatesGroup):
    choose_category = State()
    input_name = State()
    input_weight = State()
    input_shape = State()
    save_cancel = State()



