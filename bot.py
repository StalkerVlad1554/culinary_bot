from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging
from handlers import register_handlers

# Замените на ваш Telegram-бот токен
BOT_TOKEN = '7715487624:AAFsZkizvCJNO2u5FtF21fr6CPF3Z8nnULw'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# Регистрация обработчиков
register_handlers(dp)

if __name__ == '__main__':
    print("Бот запущен!")
    executor.start_polling(dp, skip_updates=True)


