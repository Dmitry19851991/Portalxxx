# my_app/urls.py

from django.urls import path
from .views import news_list, post_detail

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/<int:post_id>/', post_detail, name='post_detail'),
    # Добавьте другие маршруты, если необходимо
]
default.html - шаблон: