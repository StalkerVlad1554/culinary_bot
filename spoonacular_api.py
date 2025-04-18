import requests

# Замените на ваш API-ключ Spoonacular
API_KEY = '4de9079281184cdeb924aa65057f7be2'
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"


def get_recipe(ingredient=None):
    """
    Ищет рецепт через Spoonacular API.
    Если указан ингредиент, поиск ведется по нему, иначе используется общий запрос.
    Обрабатываются случаи, когда API не возвращает рецептов или отсутствуют
    инструкции и ингредиенты.
    """
    params = {
        'apiKey': API_KEY,
        'number': 1,  # Вернём только 1 рецепт
        'addRecipeInformation': True  # Получаем расширенную информацию о рецепте
    }

    # Если задан ингредиент, добавляем его в параметры запроса
    if ingredient:
        params['query'] = ingredient
    else:
        params['query'] = "recipe"

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            # Проверяем наличие результатов
            recipes = data.get("results", [])
            if not recipes:
                return "Рецепты по заданному запросу не найдены."

            # Выбираем первый найденный рецепт
            recipe = recipes[0]
            title = recipe.get("title", "Без названия").strip()

            # Обработка ингредиентов
            ingredients = []
            if recipe.get("extendedIngredients"):
                ingredients = [ing.get("name", "").strip() for ing in recipe["extendedIngredients"] if
                               ing.get("name", "").strip() != ""]
            if not ingredients:
                ingredients_text = "Ингредиенты отсутствуют."
            else:
                ingredients_text = "\n".join(ingredients)

            # Обработка инструкций
            instructions = recipe.get("instructions", "")
            if not instructions or instructions.strip() == "":
                instructions = "Инструкции отсутствуют или не предоставлены."

            result = (
                f"Название: {title}\n\n"
                f"Ингредиенты:\n{ingredients_text}\n\n"
                f"Инструкция:\n{instructions}"
            )
            return result
        else:
            return f"Ошибка запроса к Spoonacular API: {response.status_code}"
    except Exception as e:
        return f"Произошла ошибка при подключении к Spoonacular API: {e}"
