from aiogram import Bot, Dispatcher
import asyncio
from handlers import other_handlers, weather_by_city

from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)#Управляет командами
    dp = Dispatcher()#Принимает действия
    dp.include_routers(other_handlers.router, weather_by_city.router)
    await dp.start_polling(bot) #async and await - может делать другие процессы пока выполняеться другой
                                # dp.start_polling(bot) - Начинает слушать начинает свою работу


if __name__ == '__main__':
    asyncio.run(main())
