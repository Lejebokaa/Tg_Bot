from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates
# import aiohttp
import requests

from config import TOKEN_WHETHER

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
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN_WHETHER}&units=metric"
    req = requests.get(url).json()
    await message.reply(
        text=f"Город: {city}\n"
             f"Описание: {req['weather'][0]['main']}\n"
             f"Температура: {req['main']['temp']}\n"
             f"Часовой пояс: {req['timezone']}")


    # async with aiohttp.ClientSession as session:
    #     async with session.get(url=url, ) as response:
    #         weather_data = await response.text()
    #         print(weather_data)
