from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import User
from django import forms


class StyleFormMixin:
    """
    Миксин для стилизации форм
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'status':
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfiledFrom(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'readonly': 'readonly'})
        self.fields['password'].widget = forms.HiddenInput()


class LoginForm(StyleFormMixin, AuthenticationForm):
    pass