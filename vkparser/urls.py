from django.urls import path
from django.contrib.auth import views as auth_views
from vkparser import views


urlpatterns = [
    path('', views.vk_refresh, name="vk_refresh"),
]
