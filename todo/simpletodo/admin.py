from django.contrib import admin
from .models import *


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "create_todo", "is_status")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_status",)
    list_filter = ("is_status", "create_todo")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class SolutionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Solution, SolutionAdmin)
