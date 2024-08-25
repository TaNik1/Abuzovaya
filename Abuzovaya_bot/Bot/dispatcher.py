from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters

from DataBase.database import SessionLocal
from DataBase.models import Item
from .bot import dp
from .config import channel_id
from .message import *


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await send_main_message(user_id)


@dp.message_handler(state=CreateUser.waiting_id)
async def check_id(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    db = SessionLocal()
    try:
        user = db.query(Item).filter(Item.onewin_id == int(message.text)).first()
        if user is None:
            await bot.send_message(user_id, "id не найден")
        else:
            if user.tg_id is None:
                user.tg_id = user_id
                db.commit()
                await state.finish()
                await bot.send_message(user_id, "id успешно добавлен")
                await send_mines_message(chat_id=user_id)
            else:
                await bot.send_message(user_id, "Данный id уже используется")
    finally:
        db.close()


@dp.callback_query_handler(filters.Text(equals="check_subscription"))
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if member.is_chat_member():
        await send_main_message(chat_id=user_id, message_id=callback_query.message.message_id)
    else:
        await bot.answer_callback_query(callback_query.id, "Вы не подписаны на канал.", show_alert=True)


@dp.callback_query_handler(filters.Text(equals="coming_soon"))
async def select_games(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Скоро станет доступно", show_alert=True)


@dp.callback_query_handler(filters.Text(equals="instruction"))
async def instruction(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_instruction_message(user_id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(filters.Text(equals="registration"))
async def registration(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_registration_message(user_id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(filters.Text(equals="check_registration"))
async def check_registration(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    db = SessionLocal()
    try:
        user = db.query(Item).filter(Item.tg_id == user_id).first()
        if user is None:
            await send_check_registration(user_id, message_id=callback_query.message.message_id)
        else:
            await bot.answer_callback_query(callback_query.id, f"Вы уже зарегистрированы. Ваш id:\n{user.onewin_id}",
                                            show_alert=True)
    finally:
        db.close()


@dp.callback_query_handler(filters.Text(equals="scheme"))
async def process_scheme(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    db = SessionLocal()
    try:
        user = db.query(Item).filter(Item.tg_id == user_id).first()
        if user is None:
            await bot.answer_callback_query(callback_query.id, "Сначала пройдите регистрацию", show_alert=True)
        else:
            await send_select_scheme_message(user_id, message_id=callback_query.message.message_id)
    finally:
        db.close()


@dp.callback_query_handler(filters.Text(equals="menu"))
async def menu(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_main_message(user_id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(filters.Text(startswith="mine_"))
async def process_mine_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_select_coefficient_message(user_id, callback_query.data,
                                          message_id=callback_query.message.message_id)


@dp.callback_query_handler(filters.Text(startswith="stars_"))
async def process_stars_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if callback_query.message.text:
        await send_scheme_message(user_id, callback_query.data)
    else:
        await send_scheme_message(user_id, callback_query.data, message_id=callback_query.message.message_id)


@dp.callback_query_handler(filters.Text(equals="game_mines"))
async def select_mines_game(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    await send_mines_message(user_id, message_id=callback_query.message.message_id)
    current_state = await state.get_state()

    if current_state == CreateUser.waiting_id:
        await state.finish()
