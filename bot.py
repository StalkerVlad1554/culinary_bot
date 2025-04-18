import telebot
from handlers import register_handlers

# Замените на ваш Telegram-бот токен, полученный у BotFather
BOT_TOKEN = '7715487624:AAFsZkizvCJNO2u5FtF21fr6CPF3Z8nnULw'

bot = telebot.TeleBot(BOT_TOKEN)

# Регистрируем обработчики команд и сообщений
register_handlers(bot)

if __name__ == '__main__':
    print("Бот запущен!")
    bot.infinity_polling()