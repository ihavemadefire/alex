from django import forms
from ..models import BaseMedia
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BaseMediaForm(forms.ModelForm):
    class Meta:
        model = BaseMedia
        fields = [
            "title",
            "creator",
            "year",
            "description",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Add Media"))
