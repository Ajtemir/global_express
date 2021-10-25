import logging
import os

import psycopg2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    button_store = KeyboardButton('Склады')
    button_price = KeyboardButton('Цены')
    button_order = KeyboardButton('Заказы')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_store).add(button_price).add(button_order)
    await message.reply("Привет", reply_markup=greet_kb)


@dp.message_handler(Text(equals="Склады"))
async def store(message: types.Message):
    await message.reply("Отличный выбор!")


@dp.message_handler(Text(equals="Цены"))
async def price(message: types.Message):
    await message.reply("Отличный выбор!")


@dp.message_handler(Text(equals="Заказы"))
async def order(message: types.Message):
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    name = message.from_user.username.lower()
    cur = conn.cursor()

    cur.execute(f"""select id from users_user where telegram='{name}';""")
    text = cur.fetchone()
    owner = text[0]
    cur.execute(f"""select * from parcels where user_id='{owner}' and is_deleted='f'""")
    text = cur.fetchall()
    inline = InlineKeyboardMarkup()
    for i in text:
        inline_btn = InlineKeyboardButton(f'{i[0]}  {i[3]}', callback_data=f'pcl {i[0]}')
        inline.add(inline_btn)
    conn.close()
    await message.reply("Номера, названия товаров", reply_markup=inline)


@dp.callback_query_handler(lambda query: query.data.startswith('pcl'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    query = callback_query.data[4:(len(callback_query.data)-1)]
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute(f"""select status from parcels where id={query};""")
    text = cur.fetchone()
    conn.close()

    await bot.answer_callback_query(
        callback_query.id,
        text=f'Статус товара\n{text}', show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
