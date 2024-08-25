from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import ChatNotFound
from aiogram.dispatcher.handler import CancelHandler

CHANNEL_ID = "@ABUZOVAYA_K"


class SubscriptionMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        from Abuzovaya_bot.Bot.message import send_subscription_message

        if data.get('ignore_subscription'):
            return

        if not await self.check_subscription(message.from_user.id):
            await send_subscription_message(message.from_user.id)
            raise CancelHandler()

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        from Abuzovaya_bot.Bot.message import send_subscription_message
        if data.get('ignore_subscription'):
            return

        if not await self.check_subscription(callback_query.from_user.id):
            await send_subscription_message(chat_id=callback_query.from_user.id,
                                            inline_message_id=callback_query.inline_message_id)
            raise CancelHandler()

    @staticmethod
    async def check_subscription(user_id):
        from Abuzovaya_bot.Bot.bot import bot
        try:
            member = await bot.get_chat_member(CHANNEL_ID, user_id)
            return member.is_chat_member()
        except ChatNotFound:
            return False
