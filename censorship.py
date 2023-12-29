# my_app/templatetags/censorship.py

from django import template
import re

register = template.Library()


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        # Список нежелательных слов
        undesirable_words = ['редиска', 'нежелательное_слово_2', 'нежелательное_слово_3']

        # Цензурирование слов в строке
        for word in undesirable_words:
            pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
            value = pattern.sub('*' * len(word), value)

        return value
    else:
        raise ValueError("Фильтр censor применяется только к строкам.")

