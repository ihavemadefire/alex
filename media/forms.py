from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'creator', 'year', 'description', 'notes', 'isbn', 'publisher', 'genre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Book'))



class ISBNLookupForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Lookup ISBN'))
