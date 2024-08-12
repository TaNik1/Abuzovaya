from .bot import bot
from .States import CreateUser
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..utils.GridGenerator import GridGenerator
import aiofiles
from io import BytesIO


async def send_start_message(chat_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="Подписаться👉🏻", url="https://t.me/+NBZaJjasSl02MmY6"))
    keyboard.add(InlineKeyboardButton(text="Я уже подписан✅", callback_data="check_subscription"))

    message_text = (
        "<b>👇🏻Подпишись на канал, что бы продолжить👇🏻</b>\n\n"
        "https://t.me/+NBZaJjasSl02MmY6\n"
        "https://t.me/+NBZaJjasSl02MmY6\n"
        "https://t.me/+NBZaJjasSl02MmY6\n"
    )
    async with aiofiles.open("src/image/img5.jpg", 'rb') as photo:
        await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard)


async def send_main_message(chat_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="🔑Регистрация 1WIN🔑", url="https://telegra.ph/Registraciya-1WIN-07-28"))
    keyboard.add(InlineKeyboardButton(text="📜Инструкция📜", url="https://telegra.ph/Instrukciya-07-28-9"))
    keyboard.add(InlineKeyboardButton(text="📦Выдать схему📦", callback_data="scheme"))

    message_text = (
        "<b>📌 МЕНЮ 📌</b>\n\n"
        "⚠️ Для корректной работы софта, у вас должен быть Новый аккаунт 1win. В ином случае вы <b>не сможете получить бонус +500%</b> к первому депозиту. "
        "<a href='https://telegra.ph/Registraciya-1WIN-07-28'>🔑Регистрация 1WIN🔑</a>\n\n"
        "⚠️ Что бы играть без риска, обязательно изучите Инструкцию. "
        "<a href='https://telegra.ph/Instrukciya-07-28-9'>📜Инструкция📜</a>\n\n"
        "⚠️ Важно следовать всем данным вам инструкциям, при которых вероятность победы максимальна!\n\n"
        "👉🏻 Мы - команда по разработке схем, для обхода игр в онлайн казино. На данный момент мы с уверенностью можем продемонстрировать софт для игры Mines на 1win.\n\n"
        "👉🏻 Mines - это гемблинг игра в букмекерской конторе 1win, которая основывается на класической игре Сапёр.\n\n"
        "<b>✅ Ваша цель - следовать инструкциям и заработать свой первый кеш у нас!</b>\n\n"
        "❇️ Начинай с <b>Регистрации 👇🏻</b>\n"
        "❇️ Потом читай <b>Инструкцию 👇🏻</b>\n"
        "❇️ И приступай к игре по <b>Схемам 👇🏻</b>"
    )
    async with aiofiles.open("src/image/img1.jpg", 'rb') as photo:
        await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard)


async def send_select_scheme_message(chat_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="1💣", callback_data="mine_1"))
    keyboard.add(InlineKeyboardButton(text="3💣", callback_data="mine_3"))
    keyboard.add(InlineKeyboardButton(text="5💣", callback_data="mine_5"))
    keyboard.add(InlineKeyboardButton(text="7💣", callback_data="mine_7"))

    message_text = (
        "<b>✅Выберите кол-во мин ❌</b>"
    )
    await bot.send_message(chat_id, message_text, reply_markup=keyboard)


async def send_select_coefficient_message(chat_id, type_scheme):
    keyboard = InlineKeyboardMarkup(row_width=5)
    if type_scheme[-1] == "1":
        keyboard.add(InlineKeyboardButton(text="1.84💯", callback_data='stars_12_' + type_scheme),
                     InlineKeyboardButton(text="1.99💯", callback_data='stars_13_' + type_scheme),
                     InlineKeyboardButton(text="2.17💯", callback_data='stars_14_' + type_scheme),
                     InlineKeyboardButton(text="2.39💯", callback_data='stars_15_' + type_scheme),
                     InlineKeyboardButton(text="2.65💯", callback_data='stars_16_' + type_scheme),
                     InlineKeyboardButton(text="2.98💯", callback_data='stars_17_' + type_scheme),
                     InlineKeyboardButton(text="3.41💯", callback_data='stars_18_' + type_scheme))
    elif type_scheme[-1] == "3":
        keyboard.add(InlineKeyboardButton(text="1.93💯", callback_data='stars_5_' + type_scheme),
                     InlineKeyboardButton(text="2.27💯", callback_data='stars_6_' + type_scheme),
                     InlineKeyboardButton(text="2.69💯", callback_data='stars_7_' + type_scheme),
                     InlineKeyboardButton(text="3.23💯", callback_data='stars_8_' + type_scheme))
    elif type_scheme[-1] == "5":
        keyboard.add(InlineKeyboardButton(text="1.93💯", callback_data='stars_3_' + type_scheme),
                     InlineKeyboardButton(text="2.49💯", callback_data='stars_4_' + type_scheme),
                     InlineKeyboardButton(text="3.27💯", callback_data='stars_5_' + type_scheme))
    elif type_scheme[-1] == "7":
        keyboard.add(InlineKeyboardButton(text="1.86💯", callback_data='stars_2_' + type_scheme),
                     InlineKeyboardButton(text="2.68💯", callback_data='stars_3_' + type_scheme))
    keyboard.add(InlineKeyboardButton(text="💣Изменить кол-во мин💣", callback_data="scheme"))
    keyboard.add(InlineKeyboardButton(text="📌МЕНЮ📌", callback_data="menu"))

    message_text = (
        f"<b>✅Выберите желаемый коэффициент ({type_scheme[-1]}x💣)</b>"
    )

    await bot.send_message(chat_id, message_text, reply_markup=keyboard)


async def send_scheme_message(chat_id, stars):
    type_scheme = "_".join(stars.split("_")[2:])
    stars_count = int(stars.split("_")[1])

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="✅Забрать схему✅", callback_data=stars))
    keyboard.add(InlineKeyboardButton(text="💣Изменить кол-во мин💣", callback_data="scheme"))
    keyboard.add(InlineKeyboardButton(text="💯Изменить коэффициент💯", callback_data=type_scheme))
    keyboard.add(InlineKeyboardButton(text="📌МЕНЮ📌", callback_data="menu"))

    image = GridGenerator(stars_count).generate_grid()
    file = BytesIO()
    image.save(file, 'PNG')
    file.seek(0)
    await bot.send_photo(chat_id, file, reply_markup=keyboard)


async def send_join_request_message(chat_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="📌МЕНЮ📌", callback_data="menu"))

    message_text = (
        "<b>👋🏻Привет!👋🏻</b>\n\n"
        "⭐️Я - Бот канала <a href='https://t.me/+NBZaJjasSl02MmY6'> АБУЗОВАЯ КАЗИНО</a>⭐️\n"
        "⭐️Меня создали, что бы дать тебе Сигналы для заработка на 1win⭐️\n\n"
    )
    async with aiofiles.open("src/image/img6.jpg", 'rb') as photo:
        await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard)
    await send_check_registration(chat_id)


async def send_check_registration(chat_id):
    message_text = (
        "<b>⚠️ Для корректной работы софта, Боту необходимо привязаться к аккаунту 1win.Без этого работа сигналов - невозможна ⚠️</b>\n\n"
        "<b><a href='https://telegra.ph/Registraciya-1WIN-07-28'>🔑Регистрация 1WIN🔑</a></b>\n\n"
        "<b>✅ Введите ID из 8 цифр: ✅</b>"
    )
    async with aiofiles.open("src/image/img7.jpg", 'rb') as photo:
        await bot.send_photo(chat_id, photo, caption=message_text)
    await CreateUser.waiting_id.set()
