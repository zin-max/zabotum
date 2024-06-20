from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import default_state
from states.user import psy_test as pst

from keyboards.main_kb import main_kb as mkb
from keyboards.screening import screening as scrkb
from lexicon.welcome import WELCOME as wlc
from lexicon.scr_btns import scr_btns
from lexicon.dp_qs import dp_qs
from lexicon.anx_qs import anx_qs
from lexicon.scr_intro import scr_intro

i = 1
test = ''


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=wlc['text'][0] 
        + message.from_user.first_name 
        + wlc['text'][1],
        parse_mode='html',
        reply_markup=mkb
        )


@router.message(StateFilter(default_state) and F.text == wlc['dp_btn'])
async def start_dp_scr(message: Message, state: FSMContext):
    await message.answer(
        text=scr_intro
        )
    await message.answer(
        text=dp_qs[0],
        reply_markup=scrkb
        )
    test = 'dp'
    await state.set_state(pst.q)


@router.message(StateFilter(default_state) and F.text == wlc['anx_btn'])
async def start_dp_scr(message: Message, state: FSMContext):
    await message.answer(
        text=anx_qs[0],
        reply_markup=scrkb
    )
    test = 'anx'
    await state.set_state(pst.q)


@router.message(StateFilter(pst.q), lambda s: s.text in ''.join(scr_btns))
async def scr(message: Message, state: FSMContext):
    global i
    if i < len(anx_qs):
        await message.answer(
    text=anx_qs[i] if test == 'anx' else dp_qs[i],
                reply_markup=scrkb
            )
    else:
        await message.answer(
                text='Заботум пока не считает и не записывает результат')
        await state.set_state(default_state)
        await message.answer(
                text='Но все же можно пройти тест еще раз или выбрать дургой',
                reply_markup=mkb)
    if i < len(anx_qs):
        i += 1
        await state.set_state(pst.q)


