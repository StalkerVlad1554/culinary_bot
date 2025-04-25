from googletrans import Translator

translator = Translator()

def translate_text(text, src='auto', dest='rus'):
    """
    Переводит текст с исходного языка (src) на целевой язык (dest).
    Если src задан как 'auto', исходный язык определяется автоматически.
    """
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Ошибка при переводе: {e}"
