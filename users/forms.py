from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='نام:',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام',
            'class': 'form-control',
        })
    )

    last_name = forms.CharField(
        label='نام خانوادگی:',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام خانوادگی',
            'class': 'form-control',
        })
    )

    username = forms.CharField(
        label='نام کاربری:',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری',
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        label='ایمیل:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'ایمیل',
            'class': 'form-control',
        })
    )

    password1 = forms.CharField(
        label='رمز ورود:',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز ورود',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
        })
    )

    password2 = forms.CharField(
        label='تأیید رمز ورود:',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تأیید رمز ورود',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز ورود',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']



