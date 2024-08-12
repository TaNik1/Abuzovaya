from .bot import dp, bot
from DataBase.database import SessionLocal
from DataBase.models import Item
from aiogram import types
from .config import channel_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils.exceptions import BadRequest
from .States import CreateUser
from .message import send_main_message, send_select_scheme_message, \
    send_scheme_message, send_start_message, send_join_request_message, \
    send_select_coefficient_message, send_check_registration, send_mines_message


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    db = SessionLocal()
    try:
        user = db.query(Item).filter(Item.tg_id == user_id).first()
        if member.is_chat_member() and user is not None:
            await send_main_message(user_id)
        elif member.is_chat_member():
            await send_check_registration(user_id)
        else:
            await send_start_message(user_id)
    finally:
        db.close()


@dp.callback_query_handler(filters.Text(equals="check_subscription"))
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    if member.is_chat_member():
        await send_check_registration(user_id)
    else:
        await bot.answer_callback_query(callback_query.id, "Вы не подписаны на канал.", show_alert=True)


@dp.callback_query_handler(filters.Text(equals="scheme"))
async def process_scheme(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_select_scheme_message(user_id)


@dp.callback_query_handler(filters.Text(equals="menu"))
async def process_scheme(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_main_message(user_id)
    try:
        for i in range(callback_query.message.message_id, 0, -1):
            await bot.delete_message(callback_query.message.chat.id, i)
    except BadRequest as ex:
        pass


@dp.callback_query_handler(filters.Text(startswith="mine_"))
async def process_mine_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_select_coefficient_message(user_id, callback_query.data)


@dp.callback_query_handler(filters.Text(startswith="stars_"))
async def process_mine_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_scheme_message(user_id, callback_query.data)


@dp.callback_query_handler(filters.Text(equals="game_mines"))
async def process_mine_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await send_mines_message(user_id)


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id = update.from_user.id
    await update.approve()
    await send_join_request_message(user_id)


@dp.chat_join_request_handler(state=CreateUser.waiting_id)
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
                await send_main_message(user_id)
            else:
                await bot.send_message(user_id, "Данный id уже используется")
    finally:
        db.close()
