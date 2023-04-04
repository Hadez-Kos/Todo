from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .utils import *
from .models import *
from .forms import *


# Create your views here.


class ToDoHome(DataMixin, ListView):
    model = ToDo
    template_name = 'simpletodo/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


class CreateToDo(DataMixin, CreateView):
    model = ToDo
    form_class = AddTask
    template_name = 'simpletodo/addtask.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить задачу")
        return dict(list(context.items()) + list(c_def.items()))


class DeleteToDo(DataMixin, DeleteView):
    model = ToDo
    success_url = reverse_lazy('home')
    context_object_name = 'object'
    template_name = 'simpletodo/delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление задачи")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def login(request):
    return HttpResponse("Авторизация")
