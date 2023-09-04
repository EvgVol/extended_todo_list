from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import UsernameRegexValidator, username_me


class User(AbstractUser):

    username = models.CharField(
        'Имя пользователя',
        validators=(UsernameRegexValidator(), username_me),
        max_length=150,
        unique=True,
        blank=False,
        help_text=f'Набор символов не более 150.'
                  'Только буквы, цифры и @/./+/-/_',
        error_messages={
            'unique': "Пользователь с таким именем уже существует!",
        },
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
        blank=False,
    )

    REQUIRED_FIELDS = ('email', )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email',
            )
        ]
