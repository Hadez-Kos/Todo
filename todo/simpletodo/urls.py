from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoHome.as_view(), name='home'),
]
