from .models import *

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить задачу", "url_name": "add_task"},
    {"title": "Все задачи", "url_name": "home"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        cats = Category.objects.all()
        sols = Solution.objects.all()
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            context["posts"] = []
            user_menu.pop(1)
        elif self.request.user.is_authenticated and "is_status" in context:
            context["posts"] = ToDo.objects.filter(
                user_id=self.request.user.id, is_status=context["is_status"]
            )
        else:
            context["posts"] = ToDo.objects.filter(user_id=self.request.user.id)

        context["menu"] = user_menu
        context["cats"] = cats
        context["sols"] = sols
        return context

    def color_solution(self, objects):
        for object in objects:
            match object.name.lower():
                case "легко":
                    object.name = "panel panel-success"
                case "средне":
                    object.name = "panel panel-warning"
                case "сложно":
                    object.name = "panel panel-danger"

        return objects
