from django import forms
from .models import Category , Book


class addbook(forms.Form):
        table = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            label='ژانر',
            empty_label='انتخاب ژانر'
        )
        name = forms.CharField(label='اسم کتاب', max_length=100)
        overview = forms.CharField(label='خلاصه', max_length=100)
        image = forms.ImageField(label='تصویر', required=False)
        author = forms.CharField(label='نویسنده', max_length=100)
        created = forms.IntegerField(label='سال انتشار', required=False)

        def clean_name(self):
            name = self.cleaned_data['name'].strip()

            if Book.objects.filter(name__iexact=name).exists():
                raise forms.ValidationError(
                    'این کتاب در سایت موجود است و امکان اضافه کردن مجدد ان وجود ندارد'
                )

            return name