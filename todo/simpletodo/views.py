from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.
class ToDoHome(ListView):
    model = ToDo
    template_name = 'simpletodo/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Планировщик дел'
        return context
