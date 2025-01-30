from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardBotton

start.kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Стоимость"),
         KeyboardButton(text = "О нас")
         ]
    ]resize_keyboard = True
)


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='Средняя Игра', callback_data="medium")],
        [InlineKeyboardButton(text='Большая Игра', callback_data="big")],
        [InlineKeyboardButton(text='Очень большая Игра', callback_data="mega")],
        [InlineKeyboardButton(text='Другие предложения', callback_data="other")]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardBotton(text= 'Купить!', url = "http://ya.ru")]
    ]
)