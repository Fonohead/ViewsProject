from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': '₽',
    'usd': '$',
}

@register.filter()
def currency(value, code='rub'):
    postfix = CURRENCIES_SYMBOLS[code]
    return f'{value} {postfix}'


bad_words = []

@register.filter()
def censor(text):
    if not isinstance(text, str):
        raise TypeError("Ожидается строка, получено: " + str(type(text).__name__))

    words = text.split()  # Разбиваем на слова по пробелам
    result = []

    for word in words:
        # Извлекаем буквенную часть (убираем знаки в конце)
        clean_word = ""
        punctuation = ""
        for char in word:
            if char.isalpha():
                clean_word += char
            else:
                punctuation += char

        # Если слово пустое (например, только знаки), оставляем как есть
        if not clean_word:
            result.append(word)
            continue

        # Проверяем: если слово в списке плохих и ВСЕ буквы после первой — строчные
        if clean_word.lower() in bad_words and clean_word[1:].islower():
            # Цензурируем: первая буква + звёздочки
            censored = clean_word[0] + '*' * (len(clean_word) - 1)
            result.append(censored + punctuation)
        else:
            # Не цензурируем — оставляем как есть
            result.append(word)

    return " ".join(result)