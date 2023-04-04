from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoHome.as_view(), name='home'),
    path('delete/<pk>/', DeleteToDo.as_view(), name='delete_task')
]
