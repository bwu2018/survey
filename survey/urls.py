from django.urls import path
from . import views 

urlpatterns = [
    path('welcome/', views.welcome),
    path('create_game/', views.create_game),
    path('get_game/', views.create_game),
    path('add_answer/', views.add_answer),
    path('<slug:code>', views.add_answer),
]