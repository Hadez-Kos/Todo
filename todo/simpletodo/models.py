from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    create_todo = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_todo = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    content = models.TextField(blank=True, verbose_name="Описание")
    is_status = models.BooleanField(default=True, verbose_name="Выполнение")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="Категория"
    )
    sol = models.ForeignKey(
        "Solution", on_delete=models.PROTECT, verbose_name="Сложность"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-create_todo", "title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]


class Solution(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Сложность")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("solution", kwargs={"sol_slug": self.slug})

    class Meta:
        verbose_name = "Сложность"
        verbose_name_plural = "Сложности"
        ordering = ["id"]
