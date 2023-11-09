import logging
import handlers
import asyncio

from aiogram import Bot, Dispatcher
from config import config
from aiogram.types import BotCommand

bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp: Dispatcher = Dispatcher()
logger = logging.getLogger(__name__)

# Настроим логгирование данных
logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
# Сообщим в логах о начале работы бота
logger.info('Starting bot')

async def main():
    """
    Функция конфигурирования и запуска бота
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    dp.include_router(handlers.all_handlers.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())