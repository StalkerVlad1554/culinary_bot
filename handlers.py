from telebot import types
from spoonacular_api import get_recipe


def register_handlers(bot):
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add('Случайный рецепт', 'По ингредиенту')
        welcome_text = (
            "Привет! Я кулинарный бот, который ищет рецепты через Spoonacular API.\n"
            "Нажми 'Случайный рецепт' для получения рецепта или выбери 'По ингредиенту' для поиска по ингредиенту.\n"
            "Если выберешь второй вариант, просто введи название ингредиента в следующем сообщении."
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

    @bot.message_handler(func=lambda m: True)
    def handle_text(message):
        text = message.text.strip().lower()
        if text == "случайный рецепт":
            result = get_recipe()  # общий запрос, без фильтра по ингредиенту
            bot.send_message(message.chat.id, result)
        elif text == "по ингредиенту":
            bot.send_message(message.chat.id, "Пожалуйста, введи ингредиент, по которому искать рецепт:")
        else:
            # Если сообщение не совпадает с кнопками — считаем, что это название ингредиента
            result = get_recipe(ingredient=text)
            bot.send_message(message.chat.id, result)