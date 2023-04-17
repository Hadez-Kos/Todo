from django.test import TestCase
from simpletodo.models import *
from django.urls import reverse


# Create your tests here.


class ToDoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ToDo.objects.create(
            title="Программирование",
            content="Научиться fullstack разработке",
            is_status=True,
            slug="program",
            user_id=1,
            cat_id=4,
            sol_id=3,
        )

    def test_first_name_admin(self):
        resp = ToDo.objects.get(id=10)
        name_id = resp.user_id
        self.assertEquals(name_id, "root")
