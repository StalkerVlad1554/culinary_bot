from aiogram import types, Dispatcher
from spoonacular_api import get_recipe
from translation import translate_text
from loader import router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from key import kb_menu


@router.message(Command('start'))
async def start_handler(message: Message):
    builder = ReplyKeyboardBuilder()
    for button in kb_menu:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text="Привет! Я кулинарный бот с поддержкой перевода текста.\n\n"
        "Выбери опцию:\n"
        "• 'Случайный рецепт' для получения рецепта через Spoonacular API.\n"
        "• 'По ингредиенту' для поиска рецепта с конкретным ингредиентом.\n\n"
        "Для перевода текста используй команду:\n"
        "/translate <код_языка> <текст для перевода>",
                         reply_markup=builder.as_markup(resize_keyboard=True))



@router.message(F.text == 'Случайный рецепт')
async def random_recipe(message: Message):
    recipe = get_recipe()
    await message.reply(recipe)

@router.message(F.text == 'По ингредиенту')
async def recipe(message: Message):
    await message.reply("Введите ингредиент для поиска рецепта:")

@router.message()
async def get1_recipe(message: Message):
    ingredients = message.text
    await message.answer(get_recipe(ingredients))




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


