from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates
import aiohttp


router = Router()


@router.message(F.text == "Погода", UserStates.user_choose_button)
async def get_city_name(message: Message, state: FSMContext):
    await message.answer(
        text="Ведите название города",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choose_city)

@router.message(F.text, UserStates.user_choose_city)
async def get_city_whether(message: Message, state: FSMContext):
    city = message.text
    api = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=b8af433cff7af5d1542af7bcca7e2634&units=metric"

