from django.urls import path
from . import views 

urlpatterns = [
    path('hello/', views.say_hello),
    path('welcome/', views.welcome),
    path('game/', views.create_game),
]