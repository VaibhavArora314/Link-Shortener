from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import password_validation

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))

    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password."
        ),
        "inactive": ("This account is inactive."),
    }


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ''}))
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': '',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': '',
        }),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )


    class Meta(UserCreationForm.Meta):
        fields = ("username",)
        field_classes = {}
