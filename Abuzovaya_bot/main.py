import asyncio
from aiogram.utils import executor
from Bot.dispatcher import dp


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        executor.start_polling(dp)
    except KeyboardInterrupt:
        pass
