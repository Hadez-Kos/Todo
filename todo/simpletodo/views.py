from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.
class ToDoHome(ListView):
    model = ToDo
    template_name = 'simpletodo/home.html'
    context_object_name = 'posts'
