from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoHome.as_view(), name='home'),
    path('addtask/', CreateToDo.as_view(), name='add_task'),
    path('delete/<pk>/', DeleteToDo.as_view(), name='delete_task'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('finish/', FinishToDO.as_view(), name='fin'),
    path('working/', WorkToDO.as_view(), name='work'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task')
]
