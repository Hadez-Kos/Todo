from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить задачу", 'url_name': 'add_task'},
        {'title': "Мои задачи", 'url_name': 'home'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        cats = Category.objects.all()
        sols = Solution.objects.all()
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            context['posts'] = []
            user_menu.pop(1)
        elif self.request.user.is_authenticated and 'is_status' in context:
            context['posts'] = ToDo.objects.filter(user_id=self.request.user.id, is_status=context['is_status'])
        else:
            context['posts'] = ToDo.objects.filter(user_id=self.request.user.id)

        context['menu'] = user_menu
        context['cats'] = cats
        context['sols'] = sols
        return context
