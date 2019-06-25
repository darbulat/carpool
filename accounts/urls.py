from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('edit', views.edit, name='edit'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
