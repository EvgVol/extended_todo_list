from rest_framework import generics, permissions

from .models import Task, Category
from .pagination import LimitPageNumberPagination
from .serializers import TaskSerializer, CategorySerializer


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitPageNumberPagination
    filterset_fields = ('category',)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
