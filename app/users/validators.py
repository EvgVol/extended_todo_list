from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError


class UsernameRegexValidator(UnicodeUsernameValidator):
    """Валидация имени пользователя."""

    regex = r'^[\w.@+-]+\Z'
    flags = 0
    max_length = 150
    message = (f'Введите правильное имя пользователя. Оно может содержать'
               f' только буквы, цифры и знаки @/./+/-/_.'
               f' Длина не более 150 символов')
    error_messages = {
        'invalid': f'Набор символов не более 150. '
                   'Только буквы, цифры и @/./+/-/_',
        'required': 'Поле не может быть пустым',
    }

def username_me(value):
    """Проверка имени пользователя (me недопустимое имя)."""
    if value == 'me':
        raise ValidationError(
            'Имя пользователя "me" не разрешено.'
        )
    return value