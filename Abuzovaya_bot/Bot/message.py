import asyncio

from .bot import bot
from .States import CreateUser
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputFile, InputMediaAnimation
from aiogram.utils.exceptions import BadRequest, MessageIdentifierNotSpecified
from Abuzovaya_bot.utils.GridGenerator import GridGenerator
from io import BytesIO


async def send_subscription_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="Подписаться👉🏻", url="https://t.me/ABUZOVAYA_K"))
    keyboard.add(InlineKeyboardButton(text="Я уже подписан✅", callback_data="check_subscription"))

    message_text = (
        "<b>⚠️ Для использования Бота, нужно быть подписаным на наш канал с новостями ⚠️</b>\n\n"
        "👉🏻@ABUZOVAYA_K\n"
        "👉🏻@ABUZOVAYA_K\n"
        "👉🏻@ABUZOVAYA_K\n"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img6.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_main_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text="💣Mines💣", callback_data="game_mines"),
                 InlineKeyboardButton(text="🚀Coming Soon...", callback_data="coming_soon"),
                 InlineKeyboardButton(text="⭕️Coming Soon...", callback_data="coming_soon"),
                 InlineKeyboardButton(text="⭕️Coming Soon...", callback_data="coming_soon"),
                 InlineKeyboardButton(text="⭕️Coming Soon...", callback_data="coming_soon"),
                 InlineKeyboardButton(text="⭕️Coming Soon...", callback_data="coming_soon")
                 )

    message_text = (
        "🎮 Выберите Игру 🎮"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img1.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_mines_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="🔥Получить сигнал🔥", callback_data="scheme"))
    keyboard.add(InlineKeyboardButton(text="📜Инструкция📜", callback_data="instruction"))
    keyboard.add(InlineKeyboardButton(text="💻Регистрация 1win💻", callback_data="registration"))
    keyboard.add(InlineKeyboardButton(text="🎮Изменить игру🎮", callback_data="menu"))
    message_text = (
        "👋🏻Добро пожаловать в <b>💣Mines💣</b>\n\n"
        "<b>💣Mines</b> - это гемблинг игра от 1win, основанная на классической игре Сапёр."
        "В ней вам предстоит - открывать безопасные ячейки и не попадаться на мины!\n\n"
        "🔍Доступное кол-во мин: <b>1, 3, 5, 7</b>\n"
        "💯Доступные коэф.: <b>1.84 - 3.41</b>\n"
        "📊Точность сигнала = <b>92%</b>\n\n"
        "🆘Есть вопрос? Ответим - @ABUZOVAYA_Admin\n\n"
        "<b>🔥Начнем?👇🏻</b>"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img2.jpg")
    try:
        if message_id:
            photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img2.jpg")
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img2.jpg")
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_registration_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="💻1WIN💻", url="https://1wcght.life/casino/list?open=register&p=cnk5"))
    keyboard.add(InlineKeyboardButton(text="🔍Проверить ID🔍", callback_data="check_registration"))
    keyboard.add(InlineKeyboardButton(text="👈🏻Вернуться👈🏻", callback_data="game_mines"))
    message_text = (
        "<b>💻Регистрация 1win💻</b>\n\n"
        "1️⃣Для начала зарегистрируйтесь на сайте, нажав на кнопку\n<a "
        "href='https://1wcght.life/casino/list?open=register&p=cnk5'><b>💻1WIN💻</b></a>\n"
        "⚠️Для работы Боту нужен Новый Аккаунт 1win, что бы иметь доступ к внутренней статистике системы\n\n"
        "2️⃣Введите промокод ABUZOVAYA, он даст вам +500 % к первому депозиту\n\n"
        "3️⃣После успешной регистрации - ваша учетная запись будет автоматически проверена системой, "
        "и вы получите сообщение в боте об успешной регистрации\n"
        "⚠️Если вы зарегистрировались, но не получили сообщение, вы можете вручную проверить свой ID\n\n"
        "🆘Если вопросы, проблемы? Обращайтесь - \n@ABUZOVAYA_Admin"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img3.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_instruction_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="👈🏻Вернуться👈🏻", callback_data="game_mines"))
    message_text = (
        "<b>📜Инструкция📜</b>\n\n\n\n"
        "1️⃣Пройдите регистрацию <b>1win</b> и введите промокод <b>ABUZOVAYA</b> что бы получить <b>+500%</b> "
        "к первому депозиту\n\n"
        "2️⃣На сайте, перейдите в раздел <b>Казино - 1win games -\n💣MINES💣</b>\n\n"
        "3️⃣Нажимаете <b>🔥Получить сигнал🔥</b>\n\n"
        "4️⃣Выбирите <b>💣кол-во мин💣</b>\n\n"
        "5️⃣Выбирите <b>💯Коэффициент💯</b>\n\n"
        "6️⃣Ура! Вы получили свой первый сигнал! <b>Отыграйте поле в соответствии с Сигналом бота</b>\n\n"
        "<b>7️⃣Лутайте бабки💎</b>\n\n"
        "8️⃣Нажимайте <b>🔥Новый сигнал🔥</b> и лутаете еще раз!\n"
        "<b>⚠️Не рекомендуем играть больше 10 игр в день!</b>\n\n\n\n"
        "🆘Если вопросы, проблемы? Обращайтесь -\n@ABUZOVAYA_Admin"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img5.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_select_scheme_message(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="1💣", callback_data="mine_1"))
    keyboard.add(InlineKeyboardButton(text="3💣", callback_data="mine_3"))
    keyboard.add(InlineKeyboardButton(text="5💣", callback_data="mine_5"))
    keyboard.add(InlineKeyboardButton(text="7💣", callback_data="mine_7"))

    message_text = (
        "<b>✅Выберите кол-во мин:</b>"
    )
    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img7.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_select_coefficient_message(chat_id, type_scheme, message_id=None):
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
    message_text = (
        f"<b>✅Выберите желаемый коэффициент ({type_scheme[-1]}x💣)</b>"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img7.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)


async def send_scheme_message(chat_id, stars, message_id=None):
    with open("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/gif.gif", 'rb') as gif:
        gif = InputMediaAnimation(gif, caption=None)
        await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=gif, reply_markup=None)

    type_scheme = "_".join(stars.split("_")[2:])
    stars_count = int(stars.split("_")[1])

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="🔥Новый сигнал🔥", callback_data=stars))
    keyboard.add(InlineKeyboardButton(text="💣Изменить кол-во мин💣", callback_data="scheme"))
    keyboard.add(InlineKeyboardButton(text="💯Изменить коэффициент💯", callback_data=type_scheme))
    keyboard.add(InlineKeyboardButton(text="🚫EXIT🚫", callback_data="game_mines"))

    image = GridGenerator(stars_count).generate_grid()
    file = BytesIO()
    image.save(file, 'PNG')
    file.seek(0)

    photo = InputFile(file)
    media = InputMediaPhoto(photo, parse_mode='HTML')
    await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)


async def send_check_registration(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="👈🏻Вернуться👈🏻", callback_data="game_mines"))

    message_text = (
        "<b>✅ Введите ID аккаунта 1win из 8 цифр:</b>"
    )

    photo = InputFile("/home/nikitat612006/d/Abuzovaya/Abuzovaya_bot/src/image/img4.jpg")
    try:
        if message_id:
            media = InputMediaPhoto(photo, caption=message_text, parse_mode='HTML')
            await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=media, reply_markup=keyboard)
        else:
            await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')
    except (MessageIdentifierNotSpecified, BadRequest) as e:
        message = await bot.send_photo(chat_id, photo, caption=message_text, reply_markup=keyboard, parse_mode='HTML')

        if message.message_id > 1:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id - 1)
    await CreateUser.waiting_id.set()
