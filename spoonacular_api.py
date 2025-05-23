import requests

API_KEY = '4de9079281184cdeb924aa65057f7be2'
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

def get_recipe(ingredients=None):
    """
    Ищет рецепт через Spoonacular API.
    Можно указывать один или несколько ингредиентов.
    Обрабатываются случаи отсутствия результатов, ингредиентов и инструкций.
    """
    params = {
        'apiKey': API_KEY,
        'number': 1,  # Возвращает один рецепт
        'addRecipeInformation': True  # Расширенная информация о рецепте
    }

    if ingredients:
        if isinstance(ingredients, list):
            params['includeIngredients'] = ",".join(ingredients)  # Поиск по нескольким ингредиентам
        else:
            params['query'] = ingredients  # Поиск по одному ингредиенту

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            return f"Ошибка запроса к Spoonacular API: {response.status_code}"

        data = response.json()
        recipes = data.get("results", [])

        if not recipes:
            return "Рецепты по заданному запросу не найдены."

        recipe = recipes[0]
        recipe_id = recipe.get("id")

        if not recipe_id:
            return "Не удалось получить идентификатор рецепта."

        # Получаем подробную информацию о рецепте
        recipe_details = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/information',
                                      params={'apiKey': API_KEY})

        if recipe_details.status_code != 200:
            return f"Ошибка запроса детальной информации о рецепте: {recipe_details.status_code}"

        recipe_info = recipe_details.json()

        title = recipe_info.get("title", "Без названия").strip()

        # Обработка ингредиентов
        ingredients_list = [ing.get("name", "").strip() for ing in recipe_info.get("extendedIngredients", [])
                            if ing.get("name", "").strip()]
        ingredients_text = "\n".join(ingredients_list) if ingredients_list else "Ингредиенты отсутствуют."

        # Обработка инструкций
        instructions = recipe_info.get("instructions", "Инструкции отсутствуют или не предоставлены.")

        result = (
            f"Название: {title}\n\n"
            f"Ингредиенты:\n{ingredients_text}\n\n"
            f"Инструкция:\n{instructions}"
        )
        return result

    except Exception as e:
        return f"Произошла ошибка при подключении к Spoonacular API: {e}"

# Пример использования:

