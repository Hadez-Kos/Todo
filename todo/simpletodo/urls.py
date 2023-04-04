from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoHome.as_view(), name='home'),
    path('addtask/', CreateToDo.as_view(), name='add_task'),
    path('delete/<pk>/', DeleteToDo.as_view(), name='delete_task'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
]
