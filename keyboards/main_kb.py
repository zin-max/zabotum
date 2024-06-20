from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.welcome import WELCOME as wlc

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=wlc['dp_btn']), KeyboardButton(text=wlc['anx_btn'])]
],                              resize_keyboard=True, 
                                input_field_placeholder=wlc['placeholder'])