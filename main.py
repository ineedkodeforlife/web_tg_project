import asyncio
import logging
import json
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums.content_type import ContentType
from aiogram.filters import Command, CommandStart
from aiogram.enums.parse_mode import ParseMode

logging.basicConfig(level=logging.INFO)

bot = Bot("")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # webAppInfo = types.WebAppInfo(url="https://habr.com/ru/companies/amvera/articles/838180/")
    # builder = ReplyKeyboardBuilder()
    # builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))

    await message.answer(text='Привет!')

@dp.message(Command('site'))
async def site(message: types.Message):
    webAppInfo = types.WebAppInfo(url="https://0c84e819-78fc-4c05-8e00-d54c8dff83ca-00-r6xsqkddfyoa.kirk.replit.dev/")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))
    await message.answer(text='Привет!', reply_markup=builder.as_markup())
                         
@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    car_id = data.get('car_id')
    car_name = data.get('car_name')
    await message.answer(f'Вы выбрали машину: <b>{car_name}</b> (ID: {car_id})', parse_mode=ParseMode.HTML)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())