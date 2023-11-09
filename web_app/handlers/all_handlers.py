from main import bot, dp
from config import config

from aiogram import Router, F
from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from aiogram import Router, F
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ContentType, PhotoSize)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import InputMediaPhoto
from aiogram.filters import and_f, or_f


from geopy.distance import geodesic
from geopy.distance import distance
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import Point
from typing import List, Tuple, Dict
from copy import deepcopy

import json

from aiogram.types.web_app_info import WebAppInfo

async def send_message(message):
    await bot.send_message(config.tg_bot.admin_ids[0], message)


router: Router = Router()

@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    """
        Хэндлер для команды 'start'
    """
    # markup = ReplyKeyboardMarkup()
    # markup.add(types.KeyboardButton('Магазин', web_app=WebAppInfo(url='https://fastfruits.github.io/index.html')))

    menu_botton: KeyboardButton = KeyboardButton(text=' 🏪 Магазин ',
                                                       web_app=WebAppInfo(url='https://kolpakovee.github.io/fastfruits.github.io/index.html'))

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[menu_botton]],
                                                        resize_keybord=True)

    await message.answer(text='Привет!\n Покупай свежие фрукты у нас!', reply_markup=keyboard)

@router.message(F.content_type == 'web_app_data')
async def web_app(message: Message):
    res = json.loads(message.web_app_data.data)
    send_message(res)
    await message.answer(f'Ваш заказ принят в обраотку, с вами скоро свяжутся ваши личные сборщики фруктов!\n'
                         f'Name: {res["name"]}\n'
                         f'Email: {res["email"]}\n'
                         f'Phone: {res["phone"]}')

# @router.callback_query(CallbackQuery('test'))