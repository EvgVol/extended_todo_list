from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import UsernameRegexValidator, username_me


class SingUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UsernameRegexValidator(),]
    )

    def validate_username(self, value):
        return username_me(value)


class GetTokenSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        validators=(UsernameRegexValidator(), )
    )
    confirmation_code = serializers.CharField(required=True)

    def validate_username(self, value):
        return username_me(value)


class UsersSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            UsernameRegexValidator()
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class PersSerializer(UsersSerializer):
    pass
