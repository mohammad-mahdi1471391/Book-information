from django import forms
from .models import Category , Book


class addbook(forms.Form):
        table = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            label='Genre',
            empty_label='Select a genre'
        )
        name = forms.CharField(label='Name', max_length=100)
        overview = forms.CharField(label='Overview', max_length=100)
        image = forms.ImageField(label='Image', required=False)
        author = forms.CharField(label='Author', max_length=100)
        created = forms.IntegerField(label='Created', required=False)

        def clean_name(self):
            name = self.cleaned_data['name'].strip()

            if Book.objects.filter(name__iexact=name).exists():
                raise forms.ValidationError(
                    'This book already exists and cannot be added again.'
                )

            return name