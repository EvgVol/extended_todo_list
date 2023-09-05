from django.urls import path, include
from rest_framework import routers

from users.views import SignUp, UsersViewSet, get_token
from tasks.views import TaskViewSet, CategoryViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UsersViewSet, basename='users')
router_v1.register(r'tasks', TaskViewSet, basename='tasks')
router_v1.register(r'categories', CategoryViewSet, basename='categories')


jwt_patterns = [
    path('token/', get_token, name='get_token'),
    path('signup/', SignUp.as_view(), name='signup'),
]

urlpatterns = [
    path('v1/auth/', include(jwt_patterns)),
    path('v1/', include(router_v1.urls)),
]
