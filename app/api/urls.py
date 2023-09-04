from django.urls import path, include
from rest_framework import routers

from users.views import (SignUp, UsersViewSet, get_token)
from tasks.views import (TaskCreateAPIView, TaskListAPIView,
                         TaskDetailAPIView, CategoryListAPIView,
                         CategoryCreateAPIView,)


router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UsersViewSet, basename='users')


jwt_patterns = [
    path('token/', get_token, name='get_token'),
    path('signup/', SignUp.as_view(), name='signup'),
]

urlpatterns = [
    path('v1/auth/', include(jwt_patterns)),
    path('v1/', include(router_v1.urls)),
    path("v1/tasks/create/",
         TaskCreateAPIView.as_view(),
         name="task_create"),
    path("v1/tasks/",
         TaskListAPIView.as_view(),
         name="task_list"),
    path("v1/tasks/<int:pk>/",
         TaskDetailAPIView.as_view(),
         name="task_detail"),
    path("v1/categories/",
         CategoryListAPIView.as_view(),
         name="category_list"),
    path("v1/categories/create/",
         CategoryCreateAPIView.as_view(),
         name="category_create"),
]
