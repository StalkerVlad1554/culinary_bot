from aiogram import types, Dispatcher
from spoonacular_api import get_recipe
from translation import translate_text


async def start_handler(message: types.Message):
    """Обработчик команды /start"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Случайный рецепт", "По ингредиенту", "/translate")
    await message.reply(
        "Привет! Я кулинарный бот с поддержкой перевода текста.\n\n"
        "Выбери опцию:\n"
        "• 'Случайный рецепт' для получения рецепта через Spoonacular API.\n"
        "• 'По ингредиенту' для поиска рецепта с конкретным ингредиентом.\n\n"
        "Для перевода текста используй команду:\n"
        "/translate <код_языка> <текст для перевода>",
        reply_markup=markup,
    )


async def recipe_handler(message: types.Message):
    """Обработчик выбора рецепта"""
    text = message.text.strip().lower()
    if text == "случайный рецепт":
        recipe = await get_recipe()
        await message.reply(recipe)
    elif text == "по ингредиенту":
        await message.reply("Введите ингредиент для поиска рецепта:")
    else:
        recipe = await get_recipe(ingredient=text)
        await message.reply(recipe)


async def translate_handler(message: types.Message):
    """Обработчик команды /translate"""
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.reply("Используйте: /translate <код_языка> <текст для перевода>")
        return

    dest_lang = parts[1]
    text_to_translate = parts[2]
    translation = translate_text(text_to_translate, dest=dest_lang)
    await message.reply(translation)


def register_handlers(dp: Dispatcher):
    """Регистрация обработчиков"""
    dp.register_message_handler(start_handler, commands=["start", "help"])
    dp.register_message_handler(recipe_handler, content_types=["text"])
    dp.register_message_handler(translate_handler, commands=["translate"])
