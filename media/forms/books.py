from ..models import Book
from .base import BaseMediaForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class BookForm(BaseMediaForm):
    class Meta(BaseMediaForm.Meta):
        model = Book
        fields = BaseMediaForm.Meta.fields + [
            "isbn",
            "publisher",
            "genre",
            "fiction_non_fiction",
        ]


class ISBNLookupForm(forms.Form):
    isbn = forms.CharField(label="ISBN", max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Lookup ISBN"))
