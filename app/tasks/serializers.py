from rest_framework import serializers

from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
            slug_field='username', read_only=True, many=False, )

    class Meta:
        model = Task
        fields = '__all__'
