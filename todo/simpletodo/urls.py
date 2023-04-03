from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoHome.as_view(), name='home'),
    path('delete/<slug:post_slug>/', DeleteToDo.as_view(), name='delete_task')
]
