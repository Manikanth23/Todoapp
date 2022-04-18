from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home,name='home'),
    path('addTodoItem/',addTodoView,name='addTodoView'), 
    path('deleteTodoItem/<int:i>/',deleteTodoView,name='deleteTodoView')
]     