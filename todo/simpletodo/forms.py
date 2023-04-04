from django import forms
from .models import *


class AddTask(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ("title", "content", "is_status", "slug", "cat", "sol")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }
