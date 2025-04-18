from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('level/', views.level, name='Level'),
    path('easy/', views.easy, name='Easy'),
    path('hard/', views.hard, name='Hard'),
    path('reset_game/', views.reset_game, name = 'Reset_Game'),
]