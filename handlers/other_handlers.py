from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates

router = Router()

@router.message(Command("test")) #/test
async def test_message(message: Message):
    await message.answer("Привет, мир!!!")

@router.message(Command("dice")) #/test
async def dice(message: Message):
    await message.answer_dice("🎲")


@router.message(Command("start")) #/start
async def start(message: Message, state: FSMContext):
    await message.answer(
        text="Узнайть информацию про любой город",
        reply_markup=main_keyboard()
    )
    await state.set_state(UserStates.user_choose_button)
    