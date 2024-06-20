from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.scr_btns import scr_btns as scr

screening = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=scr[0])],
    [KeyboardButton(text=scr[1])],
    [KeyboardButton(text=scr[2])],
    [KeyboardButton(text=scr[3])],
    [KeyboardButton(text=scr[4])]
],                              resize_keyboard=True, 
                                input_field_placeholder='Нажми на одну из кнопок ниже')