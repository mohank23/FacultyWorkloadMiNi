from django.urls import path, re_path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path("index", views.index, name='index'),
    path("loginPage", views.loginPage, name='loginPage'),
    path("login", views.login, name='login'),
    path("registerPage", views.registerPage, name='registerPage'),
    path("register", views.register, name='register'),
    path("profile", views.profile, name='profile'),
    path("usersList", views.usersList, name='usersList'),

]